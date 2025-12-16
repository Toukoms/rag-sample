# RAG Sample

Learn RAG from youtube tutorial of [Tech With Tim](https://www.youtube.com/@TechWithTim).
[Video URl](https://youtu.be/AUQJ9eeP-Ls?si=njZk2Xk1ru6gq7aU)

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
