# 标书生成工具 - 全栈开发架构师提示词体系

## 一、全栈架构师角色定义

### 1.1 主角色：全栈技术架构师

```
你是一位拥有 10 年实战经验的"全栈技术架构师"，精通从需求分析到上线部署的完整技术链路。

【技术背景】
- 前端：精通 Vue3/React 生态，深入理解浏览器原理和性能优化
- 后端：精通 Python/Go/Java/Node.js，熟悉各类框架的底层实现
- 数据库：精通 MySQL/PostgreSQL/MongoDB/Redis，能进行深度调优
- DevOps：熟练使用 Docker/K8s/CI-CD，有大规模部署经验
- 主导过 30+ 项目从 0 到 1 的技术架构设计和落地实施

【核心理念】
1. 代码即文档：架构设计必须能转化为可执行的代码
2. 简单优先：能用简单方案解决的问题，绝不过度设计
3. 渐进增强：先跑起来，再优化，持续迭代
4. 实用主义：技术服务于业务，不追求技术炫技

【工作方式】
- 给出的方案必须可直接落地，包含具体代码示例
- 技术选型基于团队实际情况，不盲目追新
- 关注开发效率和维护成本的平衡
- 重视代码质量、测试覆盖、文档完善

【输出规范】
- 代码示例使用实际可运行的代码，不使用伪代码
- 配置项给出具体值，不使用"根据实际情况配置"
- 目录结构精确到文件级别
- 依赖版本明确指定

【禁止事项】
- 不输出无法运行的示例代码
- 不推荐未经验证的实验性方案
- 不忽略错误处理和边界情况
- 不设计无法维护的过度复杂架构
```

### 1.2 专项子角色

#### 前端架构师
```
你现在切换为"前端架构师"角色，专注于前端工程化和架构设计。

【技术栈精通】
- 框架：Vue 3 (Composition API)、React 18 (Hooks)、Svelte
- 构建：Vite、Webpack 5、Rollup、esbuild
- 状态管理：Pinia、Zustand、Jotai、Redux Toolkit
- 样式方案：Tailwind CSS、UnoCSS、CSS Modules、Styled Components
- 类型系统：TypeScript 5.x 深度使用
- 测试：Vitest、Jest、Playwright、Cypress

【设计原则】
1. 组件设计：单一职责、可复用、可测试
2. 状态管理：最小化全局状态、就近原则
3. 性能优先：首屏加载 < 2s、交互响应 < 100ms
4. 工程规范：ESLint + Prettier + Husky 强制执行

【输出要求】
- 组件代码必须包含 TypeScript 类型定义
- 样式方案说明具体实现方式
- 给出目录结构和文件命名规范
- 包含关键组件的完整实现代码
```

#### 后端架构师
```
你现在切换为"后端架构师"角色，专注于服务端架构和 API 设计。

【技术栈精通】
- Python：FastAPI、Django、Flask，异步编程 asyncio
- Go：Gin、Go-Zero、Kratos，并发模式
- Node.js：NestJS、Express、Fastify
- Java：Spring Boot、Spring Cloud
- 数据库：MySQL 8、PostgreSQL 15、MongoDB 7、Redis 7
- 消息队列：RabbitMQ、Kafka、Redis Streams

【设计原则】
1. API 设计：RESTful 规范、版本控制、幂等性
2. 错误处理：统一异常、优雅降级、详细日志
3. 安全防护：输入验证、SQL 注入防护、XSS 防护
4. 性能设计：连接池、缓存策略、异步处理

【输出要求】
- API 接口必须包含请求/响应的完整定义
- 数据库操作必须考虑事务和并发
- 给出完整的错误码设计
- 包含单元测试示例
```

#### 数据库架构师
```
你现在切换为"数据库架构师"角色，专注于数据层设计和优化。

【技术栈精通】
- 关系型：MySQL 8.0、PostgreSQL 15、SQLite
- 文档型：MongoDB 7、CouchDB
- 键值型：Redis 7、Memcached
- 搜索引擎：Elasticsearch 8、Meilisearch
- 向量数据库：LanceDB、Chroma、Milvus、Qdrant
- ORM：SQLAlchemy 2.0、Prisma、TypeORM、GORM

【设计原则】
1. 范式与反范式：根据查询模式选择
2. 索引策略：覆盖索引、联合索引、前缀索引
3. 分库分表：垂直拆分优先、水平拆分谨慎
4. 数据一致性：根据业务选择强一致或最终一致

【输出要求】
- 表结构必须包含完整的字段定义和索引
- 给出典型查询的 SQL 和执行计划分析
- 缓存策略必须说明失效机制
- 包含数据迁移脚本示例
```

#### DevOps 架构师
```
你现在切换为"DevOps 架构师"角色，专注于部署、运维和自动化。

【技术栈精通】
- 容器化：Docker、Podman、containerd
- 编排：Kubernetes、Docker Compose、Docker Swarm
- CI/CD：GitHub Actions、GitLab CI、Jenkins
- 监控：Prometheus、Grafana、ELK、Jaeger
- 云平台：阿里云、腾讯云、AWS、Azure

【设计原则】
1. 基础设施即代码：所有配置版本化管理
2. 不可变基础设施：镜像构建、滚动更新
3. 可观测性：日志、指标、链路追踪三位一体
4. 自动化优先：能自动化的绝不手动操作

【输出要求】
- Dockerfile 必须遵循最佳实践（多阶段构建、非 root 用户）
- K8s 配置必须包含资源限制和健康检查
- CI/CD 流水线必须可直接使用
- 监控配置必须包含告警规则
```

---

## 二、项目初始化提示词

### 2.1 项目脚手架生成

#### 2.1.1 Electron + Vue3 + TypeScript 前端项目
```
请生成 Electron + Vue3 + TypeScript 桌面应用的完整项目脚手架。

【项目要求】
- 项目名称：{{project_name}}
- 包管理器：pnpm
- UI 框架：Element Plus
- 状态管理：Pinia
- 路由：Vue Router 4
- HTTP 客户端：axios
- 构建工具：Vite 5

【输出内容】

## 1. 项目初始化命令
```bash
# 完整的初始化命令序列
```

## 2. 目录结构
```
{{project_name}}/
├── electron/                    # Electron 主进程
│   ├── main.ts                  # 主进程入口
│   ├── preload.ts               # 预加载脚本
│   ├── ipc/                     # IPC 通信模块
│   │   ├── index.ts
│   │   └── handlers/
│   └── utils/
│       └── path.ts
├── src/                         # 渲染进程（Vue）
│   ├── main.ts                  # Vue 入口
│   ├── App.vue
│   ├── router/
│   │   └── index.ts
│   ├── stores/
│   │   └── index.ts
│   ├── views/
│   │   └── Home.vue
│   ├── components/
│   │   ├── common/              # 通用组件
│   │   └── business/            # 业务组件
│   ├── composables/             # 组合式函数
│   │   └── useApi.ts
│   ├── api/                     # API 接口
│   │   ├── index.ts
│   │   ├── request.ts           # axios 封装
│   │   └── modules/
│   ├── types/                   # 类型定义
│   │   ├── global.d.ts
│   │   ├── api.d.ts
│   │   └── electron.d.ts
│   ├── styles/
│   │   ├── index.scss
│   │   └── variables.scss
│   ├── utils/
│   │   └── index.ts
│   └── assets/
├── public/
├── package.json
├── tsconfig.json
├── tsconfig.node.json
├── vite.config.ts
├── electron-builder.yml
├── .eslintrc.cjs
├── .prettierrc
└── .env.development
```

## 3. 核心配置文件

### package.json
```json
{
  "name": "{{project_name}}",
  "version": "0.1.0",
  "main": "dist-electron/main.js",
  "scripts": {
    "dev": "vite",
    "build": "vue-tsc && vite build && electron-builder",
    "preview": "vite preview",
    "lint": "eslint . --ext .vue,.js,.ts,.jsx,.tsx --fix",
    "format": "prettier --write src/"
  },
  "dependencies": {
    "vue": "^3.4.0",
    "vue-router": "^4.2.0",
    "pinia": "^2.1.0",
    "element-plus": "^2.5.0",
    "axios": "^1.6.0",
    "@vueuse/core": "^10.7.0"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^5.0.0",
    "electron": "^28.0.0",
    "electron-builder": "^24.9.0",
    "vite": "^5.0.0",
    "vite-plugin-electron": "^0.15.0",
    "vite-plugin-electron-renderer": "^0.14.0",
    "typescript": "^5.3.0",
    "vue-tsc": "^1.8.0",
    "@types/node": "^20.10.0",
    "sass": "^1.69.0",
    "unplugin-auto-import": "^0.17.0",
    "unplugin-vue-components": "^0.26.0",
    "eslint": "^8.56.0",
    "eslint-plugin-vue": "^9.19.0",
    "@typescript-eslint/eslint-plugin": "^6.15.0",
    "@typescript-eslint/parser": "^6.15.0",
    "prettier": "^3.1.0"
  }
}
```

### vite.config.ts
```typescript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import electron from 'vite-plugin-electron'
import electronRenderer from 'vite-plugin-electron-renderer'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'
import { resolve } from 'path'

export default defineConfig({
  plugins: [
    vue(),
    electron([
      {
        entry: 'electron/main.ts',
        vite: {
          build: {
            outDir: 'dist-electron',
            rollupOptions: {
              external: ['electron']
            }
          }
        }
      },
      {
        entry: 'electron/preload.ts',
        onstart(options) {
          options.reload()
        }
      }
    ]),
    electronRenderer(),
    AutoImport({
      imports: ['vue', 'vue-router', 'pinia'],
      resolvers: [ElementPlusResolver()],
      dts: 'src/types/auto-imports.d.ts'
    }),
    Components({
      resolvers: [ElementPlusResolver()],
      dts: 'src/types/components.d.ts'
    })
  ],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src')
    }
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@use "@/styles/variables.scss" as *;`
      }
    }
  }
})
```

### tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "module": "ESNext",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "preserve",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    },
    "types": ["vite/client", "node"]
  },
  "include": ["src/**/*.ts", "src/**/*.tsx", "src/**/*.vue", "electron/**/*.ts"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

## 4. 核心代码文件

### electron/main.ts
```typescript
import { app, BrowserWindow, ipcMain } from 'electron'
import { join } from 'path'

// 禁用硬件加速（解决某些系统的兼容性问题）
app.disableHardwareAcceleration()

let mainWindow: BrowserWindow | null = null

const isDev = !app.isPackaged

async function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    minWidth: 800,
    minHeight: 600,
    webPreferences: {
      preload: join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: false
    },
    show: false,
    frame: true,
    titleBarStyle: 'hiddenInset'
  })

  // 优雅显示窗口
  mainWindow.once('ready-to-show', () => {
    mainWindow?.show()
  })

  if (isDev) {
    mainWindow.loadURL('http://localhost:5173')
    mainWindow.webContents.openDevTools()
  } else {
    mainWindow.loadFile(join(__dirname, '../dist/index.html'))
  }

  mainWindow.on('closed', () => {
    mainWindow = null
  })
}

// 单实例锁
const gotTheLock = app.requestSingleInstanceLock()
if (!gotTheLock) {
  app.quit()
} else {
  app.on('second-instance', () => {
    if (mainWindow) {
      if (mainWindow.isMinimized()) mainWindow.restore()
      mainWindow.focus()
    }
  })
}

app.whenReady().then(createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow()
  }
})

// IPC 处理示例
ipcMain.handle('app:getVersion', () => app.getVersion())
```

### electron/preload.ts
```typescript
import { contextBridge, ipcRenderer } from 'electron'

// 暴露安全的 API 给渲染进程
contextBridge.exposeInMainWorld('electronAPI', {
  // 应用信息
  getVersion: () => ipcRenderer.invoke('app:getVersion'),
  
  // 窗口控制
  minimize: () => ipcRenderer.send('window:minimize'),
  maximize: () => ipcRenderer.send('window:maximize'),
  close: () => ipcRenderer.send('window:close'),
  
  // 文件操作
  openFile: (options?: Electron.OpenDialogOptions) => 
    ipcRenderer.invoke('dialog:openFile', options),
  saveFile: (options?: Electron.SaveDialogOptions) => 
    ipcRenderer.invoke('dialog:saveFile', options),
  
  // 通用 IPC
  invoke: (channel: string, ...args: any[]) => 
    ipcRenderer.invoke(channel, ...args),
  on: (channel: string, callback: (...args: any[]) => void) => {
    const subscription = (_event: Electron.IpcRendererEvent, ...args: any[]) => 
      callback(...args)
    ipcRenderer.on(channel, subscription)
    return () => ipcRenderer.removeListener(channel, subscription)
  }
})
```

### src/types/electron.d.ts
```typescript
export interface ElectronAPI {
  getVersion: () => Promise<string>
  minimize: () => void
  maximize: () => void
  close: () => void
  openFile: (options?: Electron.OpenDialogOptions) => Promise<string[] | undefined>
  saveFile: (options?: Electron.SaveDialogOptions) => Promise<string | undefined>
  invoke: (channel: string, ...args: any[]) => Promise<any>
  on: (channel: string, callback: (...args: any[]) => void) => () => void
}

declare global {
  interface Window {
    electronAPI: ElectronAPI
  }
}
```

### src/api/request.ts
```typescript
import axios, { type AxiosInstance, type AxiosRequestConfig, type AxiosResponse } from 'axios'
import { ElMessage } from 'element-plus'

// 响应数据结构
interface ApiResponse<T = any> {
  code: number
  message: string
  data: T
}

// 创建 axios 实例
const service: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8765',
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 请求拦截器
service.interceptors.request.use(
  (config) => {
    // 可在此添加 token
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    console.error('Request error:', error)
    return Promise.reject(error)
  }
)

// 响应拦截器
service.interceptors.response.use(
  (response: AxiosResponse<ApiResponse>) => {
    const { code, message, data } = response.data
    
    if (code === 200) {
      return data
    }
    
    // 业务错误
    ElMessage.error(message || '请求失败')
    return Promise.reject(new Error(message))
  },
  (error) => {
    // HTTP 错误
    const message = error.response?.data?.message || error.message || '网络错误'
    ElMessage.error(message)
    return Promise.reject(error)
  }
)

// 封装请求方法
export const request = {
  get<T>(url: string, config?: AxiosRequestConfig): Promise<T> {
    return service.get(url, config)
  },
  post<T>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T> {
    return service.post(url, data, config)
  },
  put<T>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T> {
    return service.put(url, data, config)
  },
  delete<T>(url: string, config?: AxiosRequestConfig): Promise<T> {
    return service.delete(url, config)
  }
}

export default service
```

### src/stores/index.ts
```typescript
import { createPinia } from 'pinia'
import { createPersistedState } from 'pinia-plugin-persistedstate'

const pinia = createPinia()

// 持久化插件
pinia.use(createPersistedState({
  storage: localStorage,
  key: (id) => `__pinia_${id}__`
}))

export default pinia

// 统一导出所有 store
export * from './modules/app'
export * from './modules/user'
```

### src/stores/modules/app.ts
```typescript
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAppStore = defineStore('app', () => {
  // 状态
  const sidebarCollapsed = ref(false)
  const theme = ref<'light' | 'dark'>('light')
  const language = ref('zh-CN')

  // 计算属性
  const isDark = computed(() => theme.value === 'dark')

  // 方法
  function toggleSidebar() {
    sidebarCollapsed.value = !sidebarCollapsed.value
  }

  function setTheme(newTheme: 'light' | 'dark') {
    theme.value = newTheme
    document.documentElement.setAttribute('data-theme', newTheme)
  }

  function setLanguage(lang: string) {
    language.value = lang
  }

  return {
    sidebarCollapsed,
    theme,
    language,
    isDark,
    toggleSidebar,
    setTheme,
    setLanguage
  }
}, {
  persist: true // 开启持久化
})
```
```

#### 2.1.2 Python FastAPI 后端项目
```
请生成 Python FastAPI 后端项目的完整脚手架。

【项目要求】
- 项目名称：{{project_name}}_backend
- Python 版本：3.11+
- 数据库：SQLite（开发）/ PostgreSQL（生产）
- ORM：SQLAlchemy 2.0
- 向量数据库：LanceDB
- 包管理：pip + requirements.txt

【输出内容】

## 1. 项目结构
```
{{project_name}}_backend/
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI 应用入口
│   ├── config.py                # 配置管理
│   ├── dependencies.py          # 依赖注入
│   │
│   ├── api/                     # API 路由
│   │   ├── __init__.py
│   │   ├── router.py            # 路由聚合
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── documents.py
│   │       ├── knowledge.py
│   │       ├── generation.py
│   │       └── health.py
│   │
│   ├── core/                    # 核心模块
│   │   ├── __init__.py
│   │   ├── security.py          # 安全相关
│   │   ├── exceptions.py        # 自定义异常
│   │   └── response.py          # 统一响应
│   │
│   ├── models/                  # 数据模型
│   │   ├── __init__.py
│   │   ├── base.py              # 基类
│   │   ├── document.py
│   │   └── user.py
│   │
│   ├── schemas/                 # Pydantic 模型
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── document.py
│   │   └── generation.py
│   │
│   ├── services/                # 业务逻辑
│   │   ├── __init__.py
│   │   ├── document_service.py
│   │   ├── vector_service.py
│   │   ├── llm_service.py
│   │   └── generation_service.py
│   │
│   ├── repositories/            # 数据访问层
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── document_repo.py
│   │
│   └── utils/                   # 工具函数
│       ├── __init__.py
│       ├── file_utils.py
│       └── text_utils.py
│
├── migrations/                  # 数据库迁移
│   └── versions/
│
├── tests/                       # 测试
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_api/
│   └── test_services/
│
├── scripts/                     # 脚本
│   ├── init_db.py
│   └── seed_data.py
│
├── data/                        # 数据目录
│   ├── vectors/                 # 向量数据
│   └── uploads/                 # 上传文件
│
├── templates/                   # 文档模板
│
├── .env.example
├── .env
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

## 2. 核心代码文件

### app/main.py
```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from app.config import settings
from app.api.router import api_router
from app.core.exceptions import register_exception_handlers
from app.dependencies import init_services, cleanup_services


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # 启动时初始化
    await init_services()
    print(f"🚀 {settings.APP_NAME} started on port {settings.PORT}")
    
    yield
    
    # 关闭时清理
    await cleanup_services()
    print("👋 Application shutdown complete")


def create_app() -> FastAPI:
    """创建 FastAPI 应用"""
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.VERSION,
        description="标书生成工具后端 API",
        docs_url="/docs" if settings.DEBUG else None,
        redoc_url="/redoc" if settings.DEBUG else None,
        lifespan=lifespan,
    )
    
    # 中间件
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    
    # 注册异常处理器
    register_exception_handlers(app)
    
    # 注册路由
    app.include_router(api_router, prefix="/api")
    
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info",
    )
```

### app/config.py
```python
from functools import lru_cache
from pathlib import Path
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """应用配置"""
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )
    
    # 基础配置
    APP_NAME: str = "BidGenerator"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    HOST: str = "127.0.0.1"
    PORT: int = 8765
    
    # 路径配置
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    DATA_DIR: Path = BASE_DIR / "data"
    UPLOAD_DIR: Path = DATA_DIR / "uploads"
    VECTOR_DIR: Path = DATA_DIR / "vectors"
    TEMPLATE_DIR: Path = BASE_DIR / "templates"
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]
    
    # 数据库
    DATABASE_URL: str = "sqlite+aiosqlite:///./data/app.db"
    
    # LLM 配置
    LLM_API_BASE: str = "https://api.openai.com/v1"
    LLM_API_KEY: str = ""
    LLM_MODEL: str = "gpt-4o-mini"
    LLM_TEMPERATURE: float = 0.7
    LLM_MAX_TOKENS: int = 4096
    
    # 向量模型配置
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    EMBEDDING_DIMENSION: int = 1536
    
    # 文件上传配置
    MAX_UPLOAD_SIZE: int = 50 * 1024 * 1024  # 50MB
    ALLOWED_EXTENSIONS: List[str] = [".pdf", ".docx", ".doc", ".txt", ".md"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 确保目录存在
        self.DATA_DIR.mkdir(parents=True, exist_ok=True)
        self.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        self.VECTOR_DIR.mkdir(parents=True, exist_ok=True)


@lru_cache
def get_settings() -> Settings:
    """获取配置单例"""
    return Settings()


settings = get_settings()
```

### app/core/response.py
```python
from typing import Any, Generic, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    """统一 API 响应格式"""
    code: int = 200
    message: str = "success"
    data: Optional[T] = None
    
    @classmethod
    def success(cls, data: T = None, message: str = "success") -> "ApiResponse[T]":
        return cls(code=200, message=message, data=data)
    
    @classmethod
    def error(cls, code: int = 500, message: str = "error") -> "ApiResponse":
        return cls(code=code, message=message, data=None)


class PageResponse(BaseModel, Generic[T]):
    """分页响应"""
    items: list[T]
    total: int
    page: int
    page_size: int
    pages: int
```

### app/core/exceptions.py
```python
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError


class AppException(Exception):
    """应用基础异常"""
    def __init__(
        self,
        code: int = 500,
        message: str = "Internal Server Error",
        detail: str = None
    ):
        self.code = code
        self.message = message
        self.detail = detail


class NotFoundException(AppException):
    """资源不存在"""
    def __init__(self, message: str = "Resource not found"):
        super().__init__(code=404, message=message)


class BadRequestException(AppException):
    """请求错误"""
    def __init__(self, message: str = "Bad request"):
        super().__init__(code=400, message=message)


class UnauthorizedException(AppException):
    """未授权"""
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(code=401, message=message)


def register_exception_handlers(app: FastAPI):
    """注册全局异常处理器"""
    
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        return JSONResponse(
            status_code=exc.code,
            content={
                "code": exc.code,
                "message": exc.message,
                "detail": exc.detail
            }
        )
    
    @app.exception_handler(ValidationError)
    async def validation_exception_handler(request: Request, exc: ValidationError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "code": 422,
                "message": "Validation Error",
                "detail": exc.errors()
            }
        )
    
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "code": 500,
                "message": "Internal Server Error",
                "detail": str(exc) if app.debug else None
            }
        )
```

### app/services/llm_service.py
```python
from typing import AsyncGenerator, Optional
from openai import AsyncOpenAI

from app.config import settings


class LLMService:
    """LLM 服务封装"""
    
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.LLM_API_KEY,
            base_url=settings.LLM_API_BASE,
        )
        self.model = settings.LLM_MODEL
    
    async def chat(
        self,
        messages: list[dict],
        temperature: float = None,
        max_tokens: int = None,
    ) -> str:
        """同步聊天"""
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature or settings.LLM_TEMPERATURE,
            max_tokens=max_tokens or settings.LLM_MAX_TOKENS,
        )
        return response.choices[0].message.content
    
    async def chat_stream(
        self,
        messages: list[dict],
        temperature: float = None,
    ) -> AsyncGenerator[str, None]:
        """流式聊天"""
        stream = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature or settings.LLM_TEMPERATURE,
            stream=True,
        )
        
        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    
    async def embedding(self, text: str) -> list[float]:
        """获取文本嵌入向量"""
        response = await self.client.embeddings.create(
            model=settings.EMBEDDING_MODEL,
            input=text,
        )
        return response.data[0].embedding


# 单例
llm_service = LLMService()
```

### app/services/vector_service.py
```python
from typing import Optional
import lancedb
from lancedb.pydantic import LanceModel, Vector

from app.config import settings


class DocumentChunk(LanceModel):
    """文档片段向量模型"""
    id: str
    text: str
    vector: Vector(settings.EMBEDDING_DIMENSION)
    doc_id: str
    doc_name: str
    category: str
    chunk_index: int
    metadata: dict = {}


class VectorService:
    """向量数据库服务"""
    
    def __init__(self):
        self.db: lancedb.DBConnection = None
        self.table: lancedb.table.Table = None
    
    async def init(self):
        """初始化向量数据库"""
        self.db = lancedb.connect(str(settings.VECTOR_DIR))
        
        try:
            self.table = self.db.open_table("documents")
        except Exception:
            self.table = self.db.create_table(
                "documents",
                schema=DocumentChunk,
                mode="overwrite"
            )
    
    async def add(
        self,
        chunks: list[dict],
        vectors: list[list[float]],
        doc_id: str,
        doc_name: str,
        category: str,
    ):
        """添加文档向量"""
        records = []
        for i, (chunk, vector) in enumerate(zip(chunks, vectors)):
            record = DocumentChunk(
                id=f"{doc_id}_{i}",
                text=chunk["text"],
                vector=vector,
                doc_id=doc_id,
                doc_name=doc_name,
                category=category,
                chunk_index=i,
                metadata=chunk.get("metadata", {}),
            )
            records.append(record.model_dump())
        
        if records:
            self.table.add(records)
    
    async def search(
        self,
        query_vector: list[float],
        top_k: int = 5,
        category: Optional[str] = None,
    ) -> list[dict]:
        """向量搜索"""
        search = self.table.search(query_vector).limit(top_k)
        
        if category:
            search = search.where(f"category = '{category}'")
        
        results = search.to_pandas()
        
        return [
            {
                "text": row["text"],
                "score": float(1 - row["_distance"]),
                "doc_id": row["doc_id"],
                "doc_name": row["doc_name"],
                "category": row["category"],
                "metadata": row["metadata"],
            }
            for _, row in results.iterrows()
        ]
    
    async def delete_by_doc(self, doc_id: str):
        """删除指定文档的所有向量"""
        self.table.delete(f"doc_id = '{doc_id}'")


# 单例
vector_service = VectorService()
```

### app/api/v1/generation.py
```python
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.core.response import ApiResponse
from app.services.llm_service import llm_service
from app.services.vector_service import vector_service

router = APIRouter(prefix="/generation", tags=["Generation"])


class QueryRequest(BaseModel):
    query: str
    top_k: int = 5
    category: str | None = None
    system_prompt: str | None = None


class QueryResponse(BaseModel):
    answer: str
    sources: list[dict]


@router.post("/query", response_model=ApiResponse[QueryResponse])
async def rag_query(request: QueryRequest):
    """RAG 查询接口"""
    # 1. 获取查询向量
    query_vector = await llm_service.embedding(request.query)
    
    # 2. 向量检索
    docs = await vector_service.search(
        query_vector,
        top_k=request.top_k,
        category=request.category,
    )
    
    # 3. 构建上下文
    context = "\n\n".join([
        f"【来源: {d['doc_name']}】\n{d['text']}"
        for d in docs
    ])
    
    # 4. 生成回答
    system = request.system_prompt or "你是一个专业的标书编写助手。请根据提供的参考资料回答问题。"
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": f"参考资料：\n{context}\n\n问题：{request.query}"}
    ]
    
    answer = await llm_service.chat(messages)
    
    return ApiResponse.success(QueryResponse(answer=answer, sources=docs))


@router.post("/stream")
async def rag_query_stream(request: QueryRequest):
    """RAG 流式查询接口"""
    
    async def event_generator():
        try:
            # 获取向量
            query_vector = await llm_service.embedding(request.query)
            
            # 检索
            docs = await vector_service.search(
                query_vector,
                top_k=request.top_k,
                category=request.category,
            )
            
            # 构建上下文
            context = "\n\n".join([
                f"【来源: {d['doc_name']}】\n{d['text']}"
                for d in docs
            ])
            
            system = request.system_prompt or "你是一个专业的标书编写助手。"
            messages = [
                {"role": "system", "content": system},
                {"role": "user", "content": f"参考资料：\n{context}\n\n问题：{request.query}"}
            ]
            
            # 流式生成
            async for chunk in llm_service.chat_stream(messages):
                yield f"data: {chunk}\n\n"
            
            yield "data: [DONE]\n\n"
            
        except Exception as e:
            yield f"data: [ERROR] {str(e)}\n\n"
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )
```

## 3. 配置文件

### requirements.txt
```
# Core
fastapi>=0.110.0
uvicorn[standard]>=0.27.0
pydantic>=2.6.0
pydantic-settings>=2.1.0

# Database
sqlalchemy[asyncio]>=2.0.0
aiosqlite>=0.19.0
alembic>=1.13.0

# Vector DB
lancedb>=0.5.0
pyarrow>=15.0.0

# LLM
openai>=1.12.0
tiktoken>=0.6.0

# Document Processing
python-docx>=1.1.0
docxtpl>=0.16.7
pypdf>=4.0.0
python-multipart>=0.0.9

# Utils
httpx>=0.26.0
python-magic>=0.4.27
aiofiles>=23.2.0
```

### requirements-dev.txt
```
-r requirements.txt

# Testing
pytest>=8.0.0
pytest-asyncio>=0.23.0
pytest-cov>=4.1.0
httpx>=0.26.0

# Code Quality
ruff>=0.2.0
black>=24.1.0
isort>=5.13.0
mypy>=1.8.0

# Development
ipython>=8.20.0
watchfiles>=0.21.0
```

### pyproject.toml
```toml
[tool.black]
line-length = 100
target-version = ["py311"]
include = '\.pyi?$'

[tool.isort]
profile = "black"
line_length = 100

[tool.ruff]
line-length = 100
select = ["E", "F", "W", "I", "N", "UP", "B"]
ignore = ["E501"]

[tool.mypy]
python_version = "3.11"
strict = true
ignore_missing_imports = true

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
```

### .env.example
```
# App
DEBUG=true
HOST=127.0.0.1
PORT=8765

# Database
DATABASE_URL=sqlite+aiosqlite:///./data/app.db

# LLM
LLM_API_BASE=https://api.openai.com/v1
LLM_API_KEY=your-api-key-here
LLM_MODEL=gpt-4o-mini

# Embedding
EMBEDDING_MODEL=text-embedding-3-small
```
```

---

## 三、组件开发提示词

### 3.1 前端组件开发

#### 3.1.1 通用组件开发
```
请开发一个通用的 {{component_name}} 组件。

【组件需求】
{{component_requirements}}

【设计规范】
- 遵循 Vue 3 Composition API + TypeScript
- Props 必须有完整的类型定义和默认值
- Emits 必须有类型定义
- 支持 v-model（如适用）
- 暴露必要的方法供父组件调用
- 样式使用 scoped + BEM 命名

【输出格式】

## 组件代码

### {{ComponentName}}.vue
```vue
<template>
  <!-- 模板 -->
</template>

<script setup lang="ts">
// 类型定义
interface Props {
  // ...
}

interface Emits {
  // ...
}

// Props
const props = withDefaults(defineProps<Props>(), {
  // 默认值
})

// Emits
const emit = defineEmits<Emits>()

// 状态

// 方法

// 暴露给父组件
defineExpose({
  // ...
})
</script>

<style scoped lang="scss">
// 样式
</style>
```

### 类型定义（如需要）
```typescript
// types/{{component_name}}.ts
```

### 使用示例
```vue
<!-- 使用示例 -->
```
```

#### 3.1.2 流式输出组件
```
请开发一个支持 SSE 流式输出的文本展示组件。

【功能需求】
- 接收 SSE 事件流 URL 作为数据源
- 支持打字机效果逐字显示
- 支持 Markdown 渲染
- 支持暂停/继续/停止
- 显示生成状态和进度
- 支持复制生成内容

【输出组件】

### StreamOutput.vue
```vue
<template>
  <div class="stream-output">
    <!-- 状态栏 -->
    <div class="stream-output__status">
      <span class="status-indicator" :class="statusClass"></span>
      <span class="status-text">{{ statusText }}</span>
    </div>
    
    <!-- 内容区 -->
    <div 
      ref="contentRef"
      class="stream-output__content"
      v-html="renderedContent"
    ></div>
    
    <!-- 控制栏 -->
    <div class="stream-output__actions">
      <el-button 
        v-if="status === 'streaming'"
        size="small" 
        @click="togglePause"
      >
        {{ isPaused ? '继续' : '暂停' }}
      </el-button>
      <el-button 
        v-if="status === 'streaming'"
        size="small" 
        type="danger"
        @click="stop"
      >
        停止
      </el-button>
      <el-button 
        v-if="status === 'completed'"
        size="small"
        @click="copy"
      >
        复制
      </el-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, onUnmounted } from 'vue'
import { marked } from 'marked'
import { ElMessage } from 'element-plus'

type Status = 'idle' | 'streaming' | 'paused' | 'completed' | 'error'

interface Props {
  url?: string
  autoStart?: boolean
}

interface Emits {
  (e: 'start'): void
  (e: 'chunk', chunk: string): void
  (e: 'complete', content: string): void
  (e: 'error', error: Error): void
}

const props = withDefaults(defineProps<Props>(), {
  autoStart: false
})

const emit = defineEmits<Emits>()

// 状态
const content = ref('')
const status = ref<Status>('idle')
const isPaused = ref(false)
const contentRef = ref<HTMLElement>()

let eventSource: EventSource | null = null
let pendingChunks: string[] = []

// 计算属性
const statusClass = computed(() => `status--${status.value}`)

const statusText = computed(() => {
  const texts: Record<Status, string> = {
    idle: '等待中',
    streaming: isPaused.value ? '已暂停' : '生成中...',
    paused: '已暂停',
    completed: '生成完成',
    error: '生成失败'
  }
  return texts[status.value]
})

const renderedContent = computed(() => {
  if (!content.value) return ''
  return marked(content.value)
})

// 方法
async function start(url?: string) {
  const targetUrl = url || props.url
  if (!targetUrl) {
    console.error('No URL provided')
    return
  }
  
  // 重置状态
  content.value = ''
  status.value = 'streaming'
  isPaused.value = false
  pendingChunks = []
  
  emit('start')
  
  try {
    eventSource = new EventSource(targetUrl)
    
    eventSource.onmessage = (event) => {
      const data = event.data
      
      if (data === '[DONE]') {
        complete()
        return
      }
      
      if (data.startsWith('[ERROR]')) {
        handleError(new Error(data.slice(7)))
        return
      }
      
      if (isPaused.value) {
        pendingChunks.push(data)
      } else {
        appendContent(data)
      }
    }
    
    eventSource.onerror = (error) => {
      handleError(new Error('Connection error'))
    }
    
  } catch (error) {
    handleError(error as Error)
  }
}

function appendContent(chunk: string) {
  content.value += chunk
  emit('chunk', chunk)
  scrollToBottom()
}

function scrollToBottom() {
  if (contentRef.value) {
    contentRef.value.scrollTop = contentRef.value.scrollHeight
  }
}

function togglePause() {
  isPaused.value = !isPaused.value
  
  if (!isPaused.value && pendingChunks.length > 0) {
    // 恢复时处理暂停期间的内容
    pendingChunks.forEach(chunk => appendContent(chunk))
    pendingChunks = []
  }
}

function stop() {
  eventSource?.close()
  eventSource = null
  status.value = 'completed'
  emit('complete', content.value)
}

function complete() {
  eventSource?.close()
  eventSource = null
  status.value = 'completed'
  emit('complete', content.value)
}

function handleError(error: Error) {
  eventSource?.close()
  eventSource = null
  status.value = 'error'
  emit('error', error)
}

async function copy() {
  try {
    await navigator.clipboard.writeText(content.value)
    ElMessage.success('已复制到剪贴板')
  } catch {
    ElMessage.error('复制失败')
  }
}

// 清理
onUnmounted(() => {
  eventSource?.close()
})

// 暴露方法
defineExpose({
  start,
  stop,
  togglePause,
  copy,
  content,
  status
})
</script>

<style scoped lang="scss">
.stream-output {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--el-border-color);
  border-radius: 8px;
  overflow: hidden;
  
  &__status {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 12px;
    background: var(--el-fill-color-light);
    border-bottom: 1px solid var(--el-border-color);
    
    .status-indicator {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      
      &.status--idle { background: var(--el-color-info); }
      &.status--streaming { 
        background: var(--el-color-primary);
        animation: pulse 1s infinite;
      }
      &.status--completed { background: var(--el-color-success); }
      &.status--error { background: var(--el-color-danger); }
    }
  }
  
  &__content {
    flex: 1;
    padding: 16px;
    overflow-y: auto;
    min-height: 200px;
    max-height: 500px;
    
    :deep(p) {
      margin: 0 0 1em;
      line-height: 1.6;
    }
    
    :deep(code) {
      background: var(--el-fill-color);
      padding: 2px 6px;
      border-radius: 4px;
    }
    
    :deep(pre) {
      background: var(--el-fill-color-dark);
      padding: 12px;
      border-radius: 8px;
      overflow-x: auto;
    }
  }
  
  &__actions {
    display: flex;
    gap: 8px;
    padding: 8px 12px;
    border-top: 1px solid var(--el-border-color);
  }
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
</style>
```
```

### 3.2 后端服务开发

#### 3.2.1 Service 层开发规范
```
请开发 {{service_name}} 服务层。

【业务需求】
{{business_requirements}}

【设计规范】
- Service 层处理业务逻辑，不直接操作数据库
- 依赖注入 Repository 层
- 所有方法使用 async/await
- 返回值使用 Pydantic 模型
- 异常使用自定义业务异常
- 关键操作添加日志记录

【输出格式】

## Service 代码

### services/{{service_name}}_service.py
```python
import logging
from typing import Optional

from app.core.exceptions import NotFoundException, BadRequestException
from app.repositories.{{service_name}}_repo import {{ServiceName}}Repository
from app.schemas.{{service_name}} import (
    {{ServiceName}}Create,
    {{ServiceName}}Update,
    {{ServiceName}}Response,
)

logger = logging.getLogger(__name__)


class {{ServiceName}}Service:
    """{{service_description}} 服务"""
    
    def __init__(self, repository: {{ServiceName}}Repository):
        self.repo = repository
    
    async def create(self, data: {{ServiceName}}Create) -> {{ServiceName}}Response:
        """创建"""
        logger.info(f"Creating {{service_name}}: {data.model_dump()}")
        
        # 业务校验
        # ...
        
        result = await self.repo.create(data)
        return {{ServiceName}}Response.model_validate(result)
    
    async def get_by_id(self, id: str) -> {{ServiceName}}Response:
        """根据 ID 获取"""
        result = await self.repo.get_by_id(id)
        if not result:
            raise NotFoundException(f"{{ServiceName}} not found: {id}")
        return {{ServiceName}}Response.model_validate(result)
    
    async def update(self, id: str, data: {{ServiceName}}Update) -> {{ServiceName}}Response:
        """更新"""
        existing = await self.repo.get_by_id(id)
        if not existing:
            raise NotFoundException(f"{{ServiceName}} not found: {id}")
        
        result = await self.repo.update(id, data)
        logger.info(f"Updated {{service_name}}: {id}")
        return {{ServiceName}}Response.model_validate(result)
    
    async def delete(self, id: str) -> bool:
        """删除"""
        existing = await self.repo.get_by_id(id)
        if not existing:
            raise NotFoundException(f"{{ServiceName}} not found: {id}")
        
        await self.repo.delete(id)
        logger.info(f"Deleted {{service_name}}: {id}")
        return True
    
    async def list(
        self,
        page: int = 1,
        page_size: int = 20,
        **filters
    ) -> tuple[list[{{ServiceName}}Response], int]:
        """分页列表"""
        items, total = await self.repo.list(
            offset=(page - 1) * page_size,
            limit=page_size,
            **filters
        )
        return [{{ServiceName}}Response.model_validate(item) for item in items], total
```

### 依赖注入配置
```python
# dependencies.py
from functools import lru_cache
from app.services.{{service_name}}_service import {{ServiceName}}Service
from app.repositories.{{service_name}}_repo import {{ServiceName}}Repository

@lru_cache
def get_{{service_name}}_service() -> {{ServiceName}}Service:
    repo = {{ServiceName}}Repository()
    return {{ServiceName}}Service(repo)
```

### 单元测试
```python
# tests/test_services/test_{{service_name}}_service.py
import pytest
from unittest.mock import AsyncMock, MagicMock

from app.services.{{service_name}}_service import {{ServiceName}}Service
from app.core.exceptions import NotFoundException


@pytest.fixture
def mock_repo():
    return AsyncMock()


@pytest.fixture
def service(mock_repo):
    return {{ServiceName}}Service(repository=mock_repo)


class Test{{ServiceName}}Service:
    
    async def test_get_by_id_success(self, service, mock_repo):
        # Arrange
        mock_repo.get_by_id.return_value = {"id": "1", "name": "test"}
        
        # Act
        result = await service.get_by_id("1")
        
        # Assert
        assert result.id == "1"
        mock_repo.get_by_id.assert_called_once_with("1")
    
    async def test_get_by_id_not_found(self, service, mock_repo):
        # Arrange
        mock_repo.get_by_id.return_value = None
        
        # Act & Assert
        with pytest.raises(NotFoundException):
            await service.get_by_id("not-exist")
```
```

#### 3.2.2 API 接口开发规范
```
请开发 {{resource_name}} 的 RESTful API 接口。

【接口需求】
{{api_requirements}}

【设计规范】
- 遵循 RESTful 设计原则
- 路径使用复数名词
- 使用正确的 HTTP 方法和状态码
- 统一使用 ApiResponse 封装响应
- 参数验证使用 Pydantic
- 添加 OpenAPI 文档注释

【输出格式】

### api/v1/{{resource_name}}.py
```python
from fastapi import APIRouter, Depends, Query, Path, Body, status
from typing import Optional

from app.core.response import ApiResponse, PageResponse
from app.dependencies import get_{{resource_name}}_service
from app.services.{{resource_name}}_service import {{ResourceName}}Service
from app.schemas.{{resource_name}} import (
    {{ResourceName}}Create,
    {{ResourceName}}Update,
    {{ResourceName}}Response,
    {{ResourceName}}Query,
)

router = APIRouter(prefix="/{{resource_name}}s", tags=["{{ResourceName}}"])


@router.post(
    "",
    response_model=ApiResponse[{{ResourceName}}Response],
    status_code=status.HTTP_201_CREATED,
    summary="创建{{resource_description}}",
    description="创建新的{{resource_description}}记录"
)
async def create(
    data: {{ResourceName}}Create = Body(..., description="创建数据"),
    service: {{ResourceName}}Service = Depends(get_{{resource_name}}_service)
):
    result = await service.create(data)
    return ApiResponse.success(result, "创建成功")


@router.get(
    "/{id}",
    response_model=ApiResponse[{{ResourceName}}Response],
    summary="获取{{resource_description}}详情"
)
async def get_by_id(
    id: str = Path(..., description="{{resource_description}} ID"),
    service: {{ResourceName}}Service = Depends(get_{{resource_name}}_service)
):
    result = await service.get_by_id(id)
    return ApiResponse.success(result)


@router.get(
    "",
    response_model=ApiResponse[PageResponse[{{ResourceName}}Response]],
    summary="获取{{resource_description}}列表"
)
async def list(
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(20, ge=1, le=100, description="每页数量"),
    keyword: Optional[str] = Query(None, description="搜索关键词"),
    service: {{ResourceName}}Service = Depends(get_{{resource_name}}_service)
):
    items, total = await service.list(
        page=page,
        page_size=page_size,
        keyword=keyword
    )
    
    return ApiResponse.success(PageResponse(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=(total + page_size - 1) // page_size
    ))


@router.put(
    "/{id}",
    response_model=ApiResponse[{{ResourceName}}Response],
    summary="更新{{resource_description}}"
)
async def update(
    id: str = Path(..., description="{{resource_description}} ID"),
    data: {{ResourceName}}Update = Body(..., description="更新数据"),
    service: {{ResourceName}}Service = Depends(get_{{resource_name}}_service)
):
    result = await service.update(id, data)
    return ApiResponse.success(result, "更新成功")


@router.delete(
    "/{id}",
    response_model=ApiResponse[bool],
    summary="删除{{resource_description}}"
)
async def delete(
    id: str = Path(..., description="{{resource_description}} ID"),
    service: {{ResourceName}}Service = Depends(get_{{resource_name}}_service)
):
    await service.delete(id)
    return ApiResponse.success(True, "删除成功")
```
```

---

## 四、数据库设计提示词

### 4.1 数据表设计

```
请设计 {{功能模块}} 的数据库表结构。

【业务需求】
{{business_requirements}}

【设计规范】
- 使用 SQLAlchemy 2.0 声明式模型
- 主键使用 UUID 或雪花算法
- 必须包含 created_at、updated_at 时间戳
- 软删除使用 deleted_at 字段
- 外键关系明确定义
- 索引根据查询场景设计

【输出格式】

## 1. ER 关系图（文字描述）
```
{{Entity1}} 1 ---- N {{Entity2}}
{{Entity2}} N ---- M {{Entity3}}
```

## 2. 模型代码

### models/{{model_name}}.py
```python
from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Integer, Text, DateTime, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, SoftDeleteMixin


class {{ModelName}}(Base, TimestampMixin, SoftDeleteMixin):
    """{{model_description}}"""
    
    __tablename__ = "{{table_name}}"
    
    # 主键
    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    
    # 字段
    name: Mapped[str] = mapped_column(String(100), nullable=False, comment="名称")
    description: Mapped[Optional[str]] = mapped_column(Text, comment="描述")
    status: Mapped[int] = mapped_column(Integer, default=1, comment="状态: 1-启用 0-禁用")
    
    # 外键
    category_id: Mapped[str] = mapped_column(
        String(36), 
        ForeignKey("categories.id"), 
        nullable=False,
        comment="分类ID"
    )
    
    # 关系
    category: Mapped["Category"] = relationship(back_populates="items")
    tags: Mapped[List["Tag"]] = relationship(
        secondary="{{table_name}}_tags",
        back_populates="items"
    )
    
    # 索引
    __table_args__ = (
        Index("idx_{{table_name}}_category", "category_id"),
        Index("idx_{{table_name}}_status", "status"),
        Index("idx_{{table_name}}_name", "name"),
    )
    
    def __repr__(self) -> str:
        return f"<{{ModelName}}(id={self.id}, name={self.name})>"
```

### models/base.py
```python
from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """模型基类"""
    pass


class TimestampMixin:
    """时间戳混入"""
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=func.now(),
        comment="创建时间"
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
        comment="更新时间"
    )


class SoftDeleteMixin:
    """软删除混入"""
    deleted_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime,
        nullable=True,
        comment="删除时间"
    )
    
    @property
    def is_deleted(self) -> bool:
        return self.deleted_at is not None
```

## 3. 迁移脚本

### migrations/versions/xxx_create_{{table_name}}.py
```python
"""create {{table_name}} table

Revision ID: xxx
Revises: previous_revision
Create Date: {{date}}
"""
from alembic import op
import sqlalchemy as sa

revision = 'xxx'
down_revision = 'previous_revision'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        '{{table_name}}',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('status', sa.Integer, default=1),
        sa.Column('category_id', sa.String(36), sa.ForeignKey('categories.id'), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('deleted_at', sa.DateTime, nullable=True),
    )
    
    op.create_index('idx_{{table_name}}_category', '{{table_name}}', ['category_id'])
    op.create_index('idx_{{table_name}}_status', '{{table_name}}', ['status'])


def downgrade() -> None:
    op.drop_table('{{table_name}}')
```
```

---

## 五、工程化配置提示词

### 5.1 Docker 配置

```
请生成项目的 Docker 容器化配置。

【项目结构】
- 前端：Electron + Vue3（需要打包为桌面应用）
- 后端：Python FastAPI

【输出配置】

### backend/Dockerfile
```dockerfile
# 构建阶段
FROM python:3.11-slim as builder

WORKDIR /app

# 安装构建依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 安装 Python 依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 运行阶段
FROM python:3.11-slim

WORKDIR /app

# 安装运行时依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    libmagic1 \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m -u 1000 appuser

# 从构建阶段复制依赖
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# 复制应用代码
COPY --chown=appuser:appuser . .

# 创建数据目录
RUN mkdir -p /app/data && chown -R appuser:appuser /app/data

# 切换到非 root 用户
USER appuser

# 暴露端口
EXPOSE 8765

# 健康检查
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import httpx; httpx.get('http://localhost:8765/api/health')" || exit 1

# 启动命令
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8765"]
```

### docker-compose.yml
```yaml
version: '3.8'

services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: bid-generator-backend
    ports:
      - "8765:8765"
    volumes:
      - ./backend/data:/app/data
      - ./backend/templates:/app/templates:ro
    environment:
      - DEBUG=false
      - LLM_API_KEY=${LLM_API_KEY}
      - LLM_API_BASE=${LLM_API_BASE:-https://api.openai.com/v1}
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8765/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    networks:
      - app-network

  # 如果需要数据库
  # postgres:
  #   image: postgres:15-alpine
  #   container_name: bid-generator-db
  #   environment:
  #     POSTGRES_DB: bidgenerator
  #     POSTGRES_USER: postgres
  #     POSTGRES_PASSWORD: ${DB_PASSWORD}
  #   volumes:
  #     - postgres_data:/var/lib/postgresql/data
  #   networks:
  #     - app-network

networks:
  app-network:
    driver: bridge

volumes:
  postgres_data:
```

### docker-compose.dev.yml
```yaml
version: '3.8'

services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: bid-generator-backend-dev
    ports:
      - "8765:8765"
    volumes:
      - ./backend:/app
      - ./backend/data:/app/data
    environment:
      - DEBUG=true
      - LLM_API_KEY=${LLM_API_KEY}
    command: uvicorn app.main:app --host 0.0.0.0 --port 8765 --reload
    networks:
      - app-network

networks:
  app-network:
    driver: bridge
```

### .dockerignore
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
.venv/
ENV/
.pytest_cache/
.mypy_cache/
.ruff_cache/
*.egg-info/
dist/
build/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Git
.git/
.gitignore

# Logs
*.log
logs/

# Local
.env
.env.local
*.db

# Test
tests/
coverage/
htmlcov/
```
```

### 5.2 CI/CD 配置

```
请生成 GitHub Actions CI/CD 配置。

【流水线需求】
- 代码检查：lint、type check
- 单元测试：pytest
- 构建镜像：Docker build
- 部署：推送到容器仓库

【输出配置】

### .github/workflows/ci.yml
```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  # 代码检查
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'
      
      - name: Install dependencies
        run: |
          cd backend
          pip install -r requirements-dev.txt
      
      - name: Run Ruff
        run: |
          cd backend
          ruff check .
      
      - name: Run Black
        run: |
          cd backend
          black --check .
      
      - name: Run MyPy
        run: |
          cd backend
          mypy app/

  # 单元测试
  test:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'
      
      - name: Install dependencies
        run: |
          cd backend
          pip install -r requirements-dev.txt
      
      - name: Run tests
        run: |
          cd backend
          pytest --cov=app --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./backend/coverage.xml

  # 前端检查
  frontend-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'pnpm'
      
      - name: Install pnpm
        run: npm install -g pnpm
      
      - name: Install dependencies
        run: pnpm install
      
      - name: Run ESLint
        run: pnpm lint
      
      - name: Run TypeScript check
        run: pnpm vue-tsc --noEmit

  # 构建镜像
  build:
    runs-on: ubuntu-latest
    needs: [test, frontend-lint]
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Login to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ secrets.REGISTRY_URL }}
          username: ${{ secrets.REGISTRY_USERNAME }}
          password: ${{ secrets.REGISTRY_PASSWORD }}
      
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: ./backend
          push: true
          tags: |
            ${{ secrets.REGISTRY_URL }}/bid-generator:${{ github.sha }}
            ${{ secrets.REGISTRY_URL }}/bid-generator:latest
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

### .github/workflows/release.yml
```yaml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  build-electron:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      
      - name: Install pnpm
        run: npm install -g pnpm
      
      - name: Install dependencies
        run: pnpm install
      
      - name: Build Electron app
        run: pnpm build
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: electron-${{ matrix.os }}
          path: release/**/*

  create-release:
    needs: build-electron
    runs-on: ubuntu-latest
    steps:
      - name: Download all artifacts
        uses: actions/download-artifact@v4
      
      - name: Create Release
        uses: softprops/action-gh-release@v1
        with:
          files: |
            electron-*/**/*.exe
            electron-*/**/*.dmg
            electron-*/**/*.AppImage
          draft: true
```
```

---

## 六、性能优化提示词

### 6.1 前端性能优化

```
请分析并优化以下 Vue 组件的性能问题。

【组件代码】
{{component_code}}

【性能问题分析维度】
1. 渲染性能：不必要的重渲染、大列表渲染
2. 内存泄漏：未清理的定时器、事件监听
3. 打包体积：未按需引入、大依赖
4. 网络请求：重复请求、未缓存

【输出格式】

## 1. 性能问题诊断

| 问题 | 影响 | 位置 | 严重程度 |
|------|------|------|---------|
| ... | ... | ... | 高/中/低 |

## 2. 优化方案

### 2.1 {{问题1}}
**问题描述**：...
**优化前代码**：
```vue
// 问题代码
```

**优化后代码**：
```vue
// 优化后代码
```

**优化效果**：预计提升 XX%

### 2.2 {{问题2}}
...

## 3. 通用最佳实践
- 使用 `v-memo` 缓存昂贵计算
- 大列表使用虚拟滚动
- 图片懒加载
- 组件异步加载
- ...
```

### 6.2 后端性能优化

```
请分析并优化以下 Python API 的性能问题。

【接口代码】
{{api_code}}

【性能指标】
- 当前响应时间：{{current_response_time}}
- 目标响应时间：{{target_response_time}}
- 并发量：{{concurrent_requests}}

【输出格式】

## 1. 性能瓶颈分析

### 1.1 数据库层面
- 慢查询分析
- 索引使用情况
- N+1 问题检测

### 1.2 应用层面
- CPU 密集操作
- 阻塞 I/O 操作
- 内存占用分析

### 1.3 网络层面
- 外部 API 调用
- 数据传输量

## 2. 优化方案

### 2.1 数据库优化
```python
# 优化前
# 优化后
```

### 2.2 缓存策略
```python
# 缓存实现
```

### 2.3 异步优化
```python
# 异步处理
```

## 3. 优化效果预估
| 优化项 | 预期提升 | 实现成本 |
|-------|---------|---------|
```

---

## 七、代码审查提示词

### 7.1 代码审查清单

```
请对以下代码进行全面审查。

【代码语言】：{{language}}
【代码类型】：{{code_type}} (API/组件/服务/工具)

【待审查代码】
{{code_to_review}}

【审查维度】

## 1. 代码质量
- [ ] 命名是否清晰、符合规范
- [ ] 函数/方法是否职责单一
- [ ] 是否有重复代码
- [ ] 注释是否充分且有价值
- [ ] 代码复杂度是否合理

## 2. 安全性
- [ ] 输入是否验证
- [ ] SQL 注入防护
- [ ] XSS 防护
- [ ] 敏感信息是否暴露
- [ ] 权限是否正确检查

## 3. 性能
- [ ] 是否有性能隐患
- [ ] 数据库查询是否优化
- [ ] 是否有内存泄漏风险
- [ ] 是否有不必要的计算

## 4. 可维护性
- [ ] 错误处理是否完善
- [ ] 日志是否充分
- [ ] 是否便于测试
- [ ] 是否符合团队规范

## 5. 具体问题

### 问题 1：{{问题标题}}
**位置**：第 X 行
**问题**：...
**建议**：...
**修改示例**：
```{{language}}
// 修改后的代码
```

### 问题 2：...

## 6. 总结
- 总体评价：👍 优秀 / ✅ 通过 / ⚠️ 需修改 / ❌ 需重构
- 必须修改：X 项
- 建议修改：X 项
- 亮点：...
```

---

## 八、问题排查提示词

### 8.1 Bug 排查

```
请帮我排查以下问题。

【问题描述】
{{problem_description}}

【错误信息】
{{error_message}}

【相关代码】
{{related_code}}

【环境信息】
- 操作系统：{{os}}
- 运行时版本：{{runtime_version}}
- 依赖版本：{{dependencies}}

【排查思路】

## 1. 错误分析
- 错误类型：
- 可能原因：
  1. ...
  2. ...
  3. ...

## 2. 排查步骤

### 步骤 1：{{step_description}}
```bash
# 执行命令或代码
```
预期结果：...

### 步骤 2：...

## 3. 解决方案

### 方案 A：{{solution_a}}（推荐）
```{{language}}
// 修复代码
```

### 方案 B：{{solution_b}}
```{{language}}
// 备选方案
```

## 4. 预防措施
- 添加单元测试
- 增加日志记录
- 改进错误处理
```

---

## 九、版本记录

| 版本 | 日期 | 更新内容 |
|------|------|---------|
| v1.0 | 2024-01-01 | 初始版本，全栈开发提示词体系 |
| v1.1 | 2024-03-01 | 增加组件开发模板 |
| v1.2 | 2024-05-01 | 增加性能优化和代码审查 |