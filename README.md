# RoMem 🧠

A lightweight, production-grade memory library for AI applications — built on Gemini + PostgreSQL.

---

## What is RoMem?

RoMem lets you give your AI app a **persistent memory**. Add facts, conversations, or notes — then search them semantically using natural language.

---

## Install

```bash
pip install romem
```

---

## Quick Start

```python
from romem import Memory, RoMemConfig

config = RoMemConfig(
    llm_api_key="your_gemini_api_key",
    embedding_api_key="your_gemini_api_key",
    vector_store_url="postgresql://user:password@localhost:5432/romem",
)

memory = Memory.from_config(config)

# Add memories
memory.add("I love Python and AI", user_id="rolawan")
memory.add("I am building a memory library", user_id="rolawan")

# Search
results = memory.search("what am I building?", user_id="rolawan")
for r in results:
    print(r["memory"], "→ score:", r["score"])

# Delete
memory.delete(memory_id="some-uuid")
```

---

## Features

- 🔍 **Semantic Search** — find memories by meaning, not just keywords
- 🧬 **Gemini Embeddings** — powered by Google's embedding model
- 🐘 **pgvector Storage** — fast vector search on top of PostgreSQL
- ⚡ **Concurrent Reranking** — optional LLM reranker with parallel scoring
- 🔌 **Simple API** — just `add`, `search`, `delete`, `get_all`

---

## Environment Variables

```bash
ROMEM_LLM_API_KEY=your_gemini_api_key
ROMEM_EMBEDDING_API_KEY=your_gemini_api_key
ROMEM_VECTOR_STORE_URL=postgresql://user:password@localhost:5432/romem
```

---

## Requirements

- Python 3.9+
- PostgreSQL with pgvector extension
- Gemini API key

---

## Author

Built by **Rolawan** 🚀

---

## License

MIT