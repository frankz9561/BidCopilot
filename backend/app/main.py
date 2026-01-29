from __future__ import annotations

import argparse
import json
import os
import socket
import sys
from uuid import uuid4

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import admin, health
from app.api.deps import verify_local_token
from app.api.v1.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging
from app.core.state import AppState

DEFAULT_PORT_RANGE = (8765, 8775)


def _select_available_port(preferred: int) -> int:
    if preferred and preferred != 0:
        return preferred

    start, end = DEFAULT_PORT_RANGE
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind(("127.0.0.1", port))
            except OSError:
                continue
            return port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def _emit_startup_info(port: int, token: str) -> None:
    payload = {"port": port, "token": token}
    sys.stdout.write(json.dumps(payload) + "\n")
    sys.stdout.flush()


def create_app(local_token: str | None = None, port: int | None = None) -> FastAPI:
    settings = get_settings()
    configure_logging(settings.log_level)

    app = FastAPI(title=settings.app_name, version="0.1.0")

    app.state.local_token = local_token
    app.state.port = port
    app.state.app_state = AppState(local_token=local_token, port=port)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health.router, prefix="/api")
    app.include_router(health.router, prefix="/api/v1")
    app.include_router(admin.router, prefix="/api", dependencies=[Depends(verify_local_token)])
    app.include_router(
        api_router,
        prefix="/api/v1",
        dependencies=[Depends(verify_local_token)],
    )

    return app


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    settings = get_settings()
    parser = argparse.ArgumentParser(description="BidCopilot backend service")
    parser.add_argument("--host", default=settings.host)
    parser.add_argument("--port", type=int, default=settings.port)
    parser.add_argument("--token", default=os.getenv("BIDCOPILOT_LOCAL_TOKEN", ""))
    parser.add_argument("--log-level", default=settings.log_level)
    return parser.parse_args(argv)


def main() -> None:
    args = _parse_args()
    port = _select_available_port(args.port)
    token = args.token or get_settings().local_token or uuid4().hex

    app = create_app(local_token=token, port=port)
    _emit_startup_info(port, token)

    uvicorn.run(
        app,
        host=args.host,
        port=port,
        log_level=args.log_level,
    )


if __name__ == "__main__":
    main()
