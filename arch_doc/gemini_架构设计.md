这是一套基于**技术架构师 (Technical Architect)** 视角的提示词（Prompts）套件。

这套提示词旨在帮助您利用 AI 生成**技术规格说明书 (Technical Spec)**、**架构决策记录 (ADR)**、**API 接口定义**以及**核心难点攻克方案**。它们非常具体，直接针对 **Electron + Vue3 + Python (Sidecar)** 这一混合架构的痛点。

您可以根据开发阶段，选择相应的模块直接投喂给 AI。

---

### 第一阶段：顶层架构与技术选型 (High-Level Architecture)

**目标**：确立“Electron 主导 UI，Python 主导业务”的混合架构基调，明确进程间边界。

> **Prompt 1：系统架构蓝图 (System Blueprint)**
> “请作为一名拥有 10 年经验的全栈架构师，为我设计一个‘桌面端标书生成系统’的技术架构蓝图。
> **核心约束**：
> 1. **前端壳**：Electron + Vue 3 + TypeScript (负责 UI/UX 和流式渲染)。
> 2. **核心后端**：本地运行的 Python FastAPI 子进程 (Sidecar)，负责重逻辑（RAG 检索、Word 文档生成）。
> 3. **通信**：前后端通过 HTTP (REST) 通信，而非 Node.js 原生 IPC。
> 
> 
> 请输出一份详细的 **架构设计文档 (ADD)**，包含：
> * **进程模型图 (Mermaid)**：清晰展示 Electron Main Process、Renderer Process 与 Python Sidecar 进程的启动、通信和销毁流程。
> * **端口协商机制**：详细描述如何动态分配 Python 服务的端口，并如何将该端口安全地传递给前端，防止端口冲突。
> * **生命周期管理**：当用户关闭 Electron 窗口时，如何确保后台的 Python 进程被优雅地杀死 (Graceful Shutdown)，防止僵尸进程。”
> 
> 

> **Prompt 2：架构决策记录 (ADR) - 为什么选 Python Sidecar**
> “我们需要向团队解释为什么不使用纯 Node.js 方案，而是引入 Python。请撰写一份 **ADR (Architecture Decision Record)**。
> **核心论点**：
> 1. **Word 生成能力**：对比 Node.js 的 `docxtemplater` 和 Python 的 `docxtpl`，强调 Python 在处理‘嵌套循环表格’、‘动态列’和‘Jinja2 逻辑控制’上的压倒性优势。
> 2. **RAG 生态**：强调 Python 在向量处理 (LanceDB/Chroma)、PDF 解析 (PyMuPDF) 领域的生态成熟度。
> 3. **代价与缓解**：承认引入 Python 会增加打包体积，并给出使用 `PyInstaller` 进行极致剪裁（排除 Torch/Pandas 大库）的缓解策略。”
> 
> 

---

### 第二阶段：RAG 引擎与数据层设计 (Data & AI Layer)

**目标**：设计本地向量检索的实现细节，解决性能与隐私问题。

> **Prompt 3：本地 RAG 管道设计 (RAG Pipeline Spec)**
> “请设计一套轻量级的**本地 RAG (Retrieval-Augmented Generation) 数据流**。
> **技术栈**：LanceDB (嵌入式向量库) + OpenAI Embedding API (在线)。
> 请详细描述以下流程的技术规范：
> 1. **文档摄取 (Ingestion)**：如何使用 `pdfplumber` 提取 PDF 中的复杂表格并将其转换为 Markdown 或 JSON 格式，以保留语义结构？
> 2. **分块策略 (Chunking)**：针对标书这种长文档，设计一种‘基于语义层级’的分块策略（Parent Document Retriever），确保检索到的不仅仅是碎片片段，而是完整的条款上下文。
> 3. **混合检索**：如何结合关键词搜索 (BM25) 和向量搜索 (Vector Search) 来提高检索特定标书编号或专有名词的准确率？”
> 
> 

> **Prompt 4：数据隐私与存储方案**
> “用户非常在意历史标书的隐私。请设计一套**本地数据存储方案**：
> 1. **向量库存储**：LanceDB 的文件应存储在操作系统的哪个标准目录下（AppData/Application Support）？
> 2. **源文件管理**：用户上传的 PDF 原文应如何归档？是否需要重命名或哈希校验以防重复？
> 3. **API Key 安全**：明确指出如何利用 Electron 的 `safeStorage` API 在主进程加密存储用户的 OpenAI Key，并通过内存传递给 Python 进程，严禁明文落盘。”
> 
> 

---

### 第三阶段：核心功能实现 (Core Implementation)

**目标**：针对最难的“动态 Word 生成”生成伪代码和接口定义。

> **Prompt 5：动态 Word 模板引擎接口定义**
> “核心功能是根据 RAG 检索结果自动生成 Word 标书。请定义一套 **Python 接口规范**：
> 1. **输入数据结构 (JSON Schema)**：定义前端传递给 Python 的 JSON 数据结构，需包含嵌套对象（如：`project_info`, `team_members` (list), `pricing_table` (list of lists)）。
> 2. **模板标签规范**：给出一份 Word 模板 (`.docx`) 的编写指南，展示如何使用 `docxtpl` 的 Jinja2 语法实现：
> * 动态生成表格行 (`{% tr for item in items %}`)。
> * 根据条件显示/隐藏整个段落 (`{% if has_certificate %}`)。
> 
> 
> 3. **错误处理**：当模板标签与数据不匹配时，Python 端应如何捕获异常并返回友好的错误信息给前端？”
> 
> 

> **Prompt 6：流式响应 (Streaming) 的技术实现**
> “前端需要像 ChatGPT 一样流式显示生成的标书草稿。
> 请给出 **FastAPI (Python) + Electron (Frontend)** 的流式通信代码示例：
> 1. **Python 端**：使用 `StreamingResponse` 封装 OpenAI 的生成结果。
> 2. **前端**：使用 `fetch` API 和 `TextDecoder` 逐块读取数据流并追加到 Vue 组件变量中的具体实现代码。
> 3. **中途打断**：如何实现‘停止生成’功能？（前端 AbortController -> 后端断开连接 -> 停止 LLM 请求）”
> 
> 

---

### 第四阶段：工程化与打包发布 (DevOps & Packaging)

**目标**：解决 Electron + Python 最头疼的打包和自动更新问题。

> **Prompt 7：跨平台打包与构建流水线 (Build Pipeline)**
> “请制定一份详细的 **构建与发布流程 (Build Workflow)**，针对 Windows 和 macOS 平台：
> 1. **Python 环境隔离**：如何使用 `venv` 和 `requirements.txt` 确保构建环境一致？
> 2. **PyInstaller 配置**：生成一份 `main.spec` 配置文件模板，展示如何排除无关的大型库（如 numpy, matplotlib），并将 `fastapi`, `uvicorn`, `lancedb` 正确打包为单文件或目录。
> 3. **Electron Builder 配置**：如何在 `package.json` 的 `extraResources` 字段中配置，将编译好的 Python 可执行文件复制到应用产物的正确位置？
> 4. **CI/CD 集成**：简述如何在 GitHub Actions 中自动化这套‘先编译 Python，再打包 Electron’的流程。”
> 
> 

---

### 建议的使用顺序：

1. 先用 **Prompt 1** 和 **Prompt 2** 确定整体框架，生成一份架构白皮书。
2. 用 **Prompt 7** 在项目初期就跑通“Hello World”级别的打包流程。**这一点至关重要**，因为 Electron + Python 的打包坑非常多，如果等到开发完再打包，往往会面临重构。
3. 在开发具体功能时，分别使用 **Prompt 3 (RAG)** 和 **Prompt 5 (Word生成)** 来指导代码编写。