# RAG Sample

Demonstrate utility of RAG

## Commands

Activate Environnement :

```bash
source ./.venv/Scripts/activate
```

Run fastapi server :

```bash
uv run uvicorn main:app
```

Run ingest UI :

```bash
npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery
```
