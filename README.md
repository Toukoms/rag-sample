# RAG Sample

Learn RAG from youtube tutorial of [Tech With Tim](https://www.youtube.com/@TechWithTim).<br> [Video URL](https://youtu.be/AUQJ9eeP-Ls?si=njZk2Xk1ru6gq7aU)

## Commands

Sync uv project :

```bash
uv sync
```

Activate Environnement :

```bash
source ./.venv/Scripts/activate
```

or 

```bash
source ./.venv/bin/activate
```

Run fastapi server :

```bash
uv run uvicorn main:app
```

Run ingest UI :

```bash
npx inngest-cli@latest dev -u http://localhost:8000/api/inngest --no-discovery
```

Run streamlit app :

```bash
uv run streamlit run ./streamlit_app.py
```
