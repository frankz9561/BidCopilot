from __future__ import annotations

from fastapi import Header, HTTPException, Request, status


def verify_local_token(
    request: Request,
    x_local_token: str | None = Header(default=None, alias="X-Local-Token"),
) -> None:
    token = getattr(request.app.state, "local_token", None)
    if token is None:
        return
    if x_local_token != token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid local token",
        )
