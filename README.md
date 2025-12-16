# RAG Sample

Learn RAG from youtube tutorial of [Tech With Tim](https://www.youtube.com/@TechWithTim).<br> [Video URL](https://youtu.be/AUQJ9eeP-Ls?si=njZk2Xk1ru6gq7aU)

## Commands

### 1. Sync UV Project

Install and sync project dependencies:

```bash
uv sync
```

### 2. Activate Virtual Environment

On Windows:

```bash
source ./.venv/Scripts/activate
```

On macOS/Linux:

```bash
source ./.venv/bin/activate
```

### 3. Run Qdrant Container

Start the Qdrant vector database using Docker:

```bash
docker-compose up -d
```

### 4. Run FastAPI Server

Start the API server:

```bash
uv run uvicorn main:app
```

### 5. Run Inngest Development UI

Launch the Inngest development interface for monitoring background jobs:

```bash
npx inngest-cli@latest dev -u http://localhost:8000/api/inngest --no-discovery
```

### 6. Run Streamlit Application

Start the Streamlit web interface:

```bash
uv run streamlit run ./streamlit_app.py
```

