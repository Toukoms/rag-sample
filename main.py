import logging
from fastapi import FastAPI
from dotenv import load_dotenv
import os
import inngest
from inngest import fast_api
from inngest.experimental import ai
from src.types import RAGChunkAndSrc, RAGUpsertResult
from src.data_loader import load_and_chunk_pdf, embed_texts
import uuid
from src.vector_db import QdrantStorage

load_dotenv()

inngest_client = inngest.Inngest(
  app_id="rag_app",
  logger=logging.getLogger("uvicorn"),
  is_production=os.getenv("ENV") == "production",
  serializer=inngest.PydanticSerializer()
)

qdrant_storage = QdrantStorage()

@inngest_client.create_function(
  fn_id="RAG: ingest PDF",
  trigger=inngest.TriggerEvent(event="rag/ingest_pdf"),
)
async def rag_ingest_pdf(ctx: inngest.Context):
  async def _load(ctx) -> RAGChunkAndSrc:
    pdf_path = ctx.event.data["pdf_path"]
    source_id = ctx.event.data.get("source_id", pdf_path)
    chunks = load_and_chunk_pdf(pdf_path)
    return RAGChunkAndSrc(chunks=chunks, source_id=source_id)
  
  async def _upsert(chunks_and_src: RAGChunkAndSrc) -> RAGUpsertResult:
    chunks = chunks_and_src.chunks
    source_id = chunks_and_src.source_id
    vectors = embed_texts(chunks)
    ids = [str(uuid.uuid5(uuid.NAMESPACE_URL, f"{source_id}:{i}")) for i in range(len(chunks))]
    payloads = [
      {
        "text": chunk,
        "source": source_id
      }
      for chunk in chunks
    ]
    qdrant_storage.upsert_vectors(ids, vectors, payloads)
    return RAGUpsertResult(ingested=len(chunks))
  
  chunks_and_src = await ctx.step.run("load-and-chunk", lambda: _load(ctx), output_type=RAGChunkAndSrc)
  ingested = await ctx.step.run("embed-and-upsert", lambda: _upsert(chunks_and_src), output_type=RAGUpsertResult)
  
  return ingested.model_dump()

app = FastAPI()

fast_api.serve(app, inngest_client, [rag_ingest_pdf])

