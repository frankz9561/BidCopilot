# BidCopilot Backend

FastAPI 后端服务

## 依赖管理

### 安装依赖

项目使用 `requirements.txt` 管理 Python 依赖。

#### 方式一：使用虚拟环境（推荐）

```bash
# 1. 创建虚拟环境
python -m venv venv

# 2. 激活虚拟环境
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Windows CMD:
.\venv\Scripts\activate.bat
# Linux/Mac:
source venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt
```

#### 方式二：直接安装（不推荐）

```bash
pip install -r requirements.txt
```

### 更新依赖

当添加新的依赖包时：

```bash
# 1. 安装新包
pip install <package-name>

# 2. 更新 requirements.txt
pip freeze > requirements.txt
```

或者手动编辑 `requirements.txt`，然后运行：

```bash
pip install -r requirements.txt
```

### 开发依赖（可选）

如果需要区分开发和生产依赖，可以创建 `requirements-dev.txt`：

```bash
# 包含所有生产依赖
-r requirements.txt

# 开发工具
pytest>=8.0.0
black>=24.0.0
ruff>=0.5.0
```

### 使用 pip-tools（高级，可选）

对于更严格的依赖管理，可以使用 `pip-tools`：

```bash
# 安装 pip-tools
pip install pip-tools

# 创建 requirements.in（手动编辑，只包含直接依赖）
# 然后运行：
pip-compile requirements.in

# 更新依赖：
pip-compile --upgrade requirements.in
```

## 运行项目

```bash
# 激活虚拟环境后
python main.py

# 或使用 uvicorn 直接运行
uvicorn app.main:app --reload
```

## 项目结构

```
backend/
├── app/              # 应用主代码
│   ├── api/         # API 路由
│   ├── core/        # 核心配置
│   ├── db/          # 数据库相关
│   ├── schemas/     # Pydantic 模型
│   └── utils/       # 工具函数
├── main.py          # 入口文件
└── requirements.txt # 依赖列表
```
