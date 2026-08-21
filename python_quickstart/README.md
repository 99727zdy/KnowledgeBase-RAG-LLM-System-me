# Python Quickstart (for reading this RAG project)

This folder = **Python basics** ∪ **syntax needed to read this repo**.

Learn by folder number. Run any script directly:

```bash
python 01_basics/01_variables_types.py
```

## Learning order

| # | Folder | Related project files |
|---|--------|------------------------|
| 01 | basics | everywhere; encode/decode for upload & MD5 |
| 02 | data_structures | `session_state`, metadata, config dicts |
| 03 | control_flow | dedupe checks, message loops |
| 04 | functions | functions & nested defs in `knowledge_base` / `rag` |
| 05 | oop | `KnowledgeBaseService`, `RagService`, etc. |
| 06 | modules_packages | `import config_data as config` |
| 07 | files_json | MD5 file, chat history, `store.json` |
| 08 | exceptions | upload failure, broken JSON |
| 09 | typing_and_annotations | read `list[str]`, `-> None` |
| 10 | advanced_for_project | MD5 dedupe, pipeline intuition |
| 11 | mini_project_mirror | tiny mirrors of real modules |

## After finishing, read the project in this order

1. `config_data.py`
2. `knowledge_base.py`
3. `vector_stores.py`
4. `file_history_store.py`
5. `rag.py`
6. `app_upload.py` / `app_chat.py`
