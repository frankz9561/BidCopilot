# BidCopilot 数据库设计文档

**文档版本**：v1.0  
**最后更新**：2026-01-29  
**范围**：结合《最终架构设计方案》《产品设计_最终方案》输出数据库（SQLite + LanceDB + 本地文件）设计

---

## 1. 目标与设计原则

- **本地优先**：所有业务数据存储在本地（SQLite + LanceDB + 文件系统）。
- **可追溯**：关键生成内容必须关联证据来源与版本信息。
- **可审阅**：草稿、审阅报告、风险提示结构化持久化。
- **可演进**：模块化实体设计，便于后续扩展（版本对比、审计日志、A/B 提示词）。

---

## 2. 数据存储架构

### 2.1 组件划分

- **SQLite（元数据/业务数据）**：项目、文档元信息、合规矩阵、检索计划、草稿、审阅报告、模板映射、任务记录、用户设置等。
- **LanceDB（向量与分块）**：文档分块与向量索引（RAG 证据检索）。
- **本地文件系统**：原始文件（RFP/历史标书/模板）、导出文件、缓存与日志。

### 2.2 本地目录结构（建议）

```
data/
  db.sqlite
  lancedb/
files/
  documents/
templates/
cache/
logs/
```

---

## 3. 逻辑数据模型概览

### 3.1 核心实体与关系

- **Project** 1 ─── N **Document**
- **Document** 1 ─── N **DocumentChunk（LanceDB）**
- **Project** 1 ─── N **Requirement（合规矩阵）**
- **Requirement** 1 ─── 1 **QueryPack**
- **Requirement** 1 ─── N **EvidenceItem**（指向 Chunk）
- **Project** 1 ─── N **Draft（章节草稿，含版本）**
- **Draft** 1 ─── 1 **ReviewReport**
- **Project** 1 ─── N **GenerationTask**
- **Template** 1 ─── 1 **TemplateMapping**

---

## 4. SQLite 物理设计

> 说明：JSON 字段使用 SQLite 的 JSON1 扩展；若无 JSON1，可退化为 TEXT 存储。

### 4.1 表结构（核心）

```sql
-- 项目表
CREATE TABLE projects (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    rfp_doc_id TEXT,                      -- 关联招标文件（documents.id）
    status TEXT DEFAULT 'active',         -- active/archived
    metadata JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 文档表
CREATE TABLE documents (
    id TEXT PRIMARY KEY,                  -- UUID
    project_id TEXT,                      -- 可为空（公共知识库）
    name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    file_hash TEXT NOT NULL,              -- SHA256 去重
    file_size INTEGER,
    category TEXT,                        -- 技术/商务/案例等
    status TEXT DEFAULT 'processing',     -- processing/ready/failed
    total_chunks INTEGER,
    metadata JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE SET NULL
);

-- 合规矩阵 / 需求条款
CREATE TABLE requirements (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    section TEXT,
    requirement_text TEXT NOT NULL,
    score_weight REAL,
    risk_level TEXT,                      -- high/medium/low
    status TEXT DEFAULT 'open',
    source_chunk_ids JSON,                -- 需求来源证据
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Query Pack
CREATE TABLE query_packs (
    id TEXT PRIMARY KEY,
    requirement_id TEXT NOT NULL,
    queries JSON,
    must_have_evidence JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(requirement_id) REFERENCES requirements(id) ON DELETE CASCADE
);

-- Evidence Pack
CREATE TABLE evidence_items (
    id TEXT PRIMARY KEY,
    requirement_id TEXT,
    chunk_id TEXT NOT NULL,               -- LanceDB chunk_id
    doc_id TEXT NOT NULL,
    score REAL,
    tags JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(requirement_id) REFERENCES requirements(id) ON DELETE SET NULL,
    FOREIGN KEY(doc_id) REFERENCES documents(id) ON DELETE CASCADE
);

-- 草稿版本
CREATE TABLE drafts (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    section TEXT NOT NULL,
    version INTEGER NOT NULL,
    content TEXT NOT NULL,
    citations JSON,
    prompt_version TEXT,
    status TEXT DEFAULT 'draft',          -- draft/reviewed/final
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- 审查报告
CREATE TABLE review_reports (
    id TEXT PRIMARY KEY,
    draft_id TEXT NOT NULL,
    missing_citations JSON,
    weak_support JSON,
    overclaims JSON,
    risk_flags JSON,
    suggestions JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(draft_id) REFERENCES drafts(id) ON DELETE CASCADE
);

-- 模板与映射
CREATE TABLE templates (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    schema JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE template_mappings (
    id TEXT PRIMARY KEY,
    template_id TEXT NOT NULL,
    mapping JSON NOT NULL,
    validation_rules JSON,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(template_id) REFERENCES templates(id) ON DELETE CASCADE
);

-- 生成任务
CREATE TABLE generation_tasks (
    id TEXT PRIMARY KEY,
    project_id TEXT,
    draft_id TEXT,
    task_type TEXT NOT NULL,              -- technical/commercial/pricing/review
    stage TEXT,                           -- parse/plan/draft/review/export
    status TEXT DEFAULT 'pending',        -- pending/running/completed/failed
    input_params JSON,
    prompt_version TEXT,
    evidence_refs JSON,
    output_content TEXT,
    citations JSON,
    tokens_used INTEGER,
    duration_seconds REAL,
    error_message TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE SET NULL,
    FOREIGN KEY(draft_id) REFERENCES drafts(id) ON DELETE SET NULL
);

-- 用户配置
CREATE TABLE user_settings (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 索引
CREATE INDEX idx_documents_project ON documents(project_id);
CREATE INDEX idx_documents_category ON documents(category);
CREATE INDEX idx_documents_status ON documents(status);
CREATE INDEX idx_requirements_project ON requirements(project_id);
CREATE INDEX idx_drafts_project ON drafts(project_id);
CREATE INDEX idx_tasks_status ON generation_tasks(status);
CREATE INDEX idx_tasks_created ON generation_tasks(created_at DESC);
```

### 4.2 字段说明（摘要）

- `projects.rfp_doc_id`：指向主招标文件（documents.id）。
- `documents.file_hash`：导入去重；同一项目可基于策略允许重复。
- `requirements.source_chunk_ids`：需求来源证据，便于追溯。
- `drafts.citations`：生成文本中的引用映射表（chunk_id → 片段位置）。
- `generation_tasks.evidence_refs`：任务执行时使用的证据清单。

---

## 5. LanceDB 物理设计（向量数据）

```python
from lancedb.pydantic import LanceModel, Vector

class DocumentChunk(LanceModel):
    # 主键
    id: str                                # chunk_uuid

    # 文档关联
    doc_id: str                            # 关联 documents 表
    doc_name: str                          # 文档名称（冗余）

    # 内容
    text: str                              # 原始文本
    vector: Vector(1536)                   # Embedding 向量
    text_hash: str                         # 内容哈希

    # 位置信息
    chunk_index: int
    page_number: Optional[int]
    section_title: Optional[str]
    parent_id: Optional[str]
    tokens: Optional[int]

    # 元数据
    category: str                          # 继承 document.category
    source_type: Optional[str]             # rfp/history/template
    metadata: dict

    # 时间戳
    created_at: datetime
```

---

## 6. 数据一致性与生命周期

### 6.1 导入事务（核心流程）

- 插入 `documents`（status=processing）
- 解析与分块 → 写入 LanceDB
- 更新 `documents`（status=ready + total_chunks）
- 失败回滚 → 标记失败并清理向量

### 6.2 删除级联

- 删除 `documents` → 清理 LanceDB 对应 chunk → 删除原始文件（可配置保留）。

---

## 7. 建议扩展表（满足产品路线）

> 以下为与产品功能强相关、但非 MVP 必要表，可按阶段引入。

```sql
-- 审计日志（关键操作可追溯）
CREATE TABLE audit_logs (
    id TEXT PRIMARY KEY,
    project_id TEXT,
    action TEXT NOT NULL,              -- import/generate/export/delete
    actor TEXT,                        -- 预留：本地用户/系统
    detail JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 标签系统（知识库管理）
CREATE TABLE tags (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);
CREATE TABLE document_tags (
    document_id TEXT NOT NULL,
    tag_id TEXT NOT NULL,
    PRIMARY KEY (document_id, tag_id)
);

-- 版本快照（项目回放/对比）
CREATE TABLE project_versions (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    version INTEGER NOT NULL,
    snapshot JSON NOT NULL,            -- 关键文档/草稿索引
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 8. 备份与迁移

- **备份内容**：`db.sqlite` + `lancedb/` + `templates/` + `files/`。
- **导入校验**：检查版本号与 schema 兼容性，不兼容时提示“只读导入/升级迁移”。

---

## 9. 约束与性能建议

- 为高频查询字段建立索引（project_id、status、created_at）。
- 文档大规模导入时启用批量写入与事务。
- 大型 JSON 字段可考虑拆分到子表（如 citations、evidence_refs）。

---

## 10. 版本与演进

- 所有 schema 变更使用迁移脚本记录（如 Alembic）。
- 重要字段变更需保持向后兼容，避免破坏旧项目导入。

---

**完成状态**：可用于 MVP 实施与后续扩展的数据库设计基线。
