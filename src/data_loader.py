from pathlib import Path
from openai import OpenAI
from llama_index.core.text_splitter import SentenceSplitter
from llama_index.readers.file import PDFReader
from src.env import env

client = OpenAI(
  base_url=env.OPENAI_API_BASE_URL,
  api_key=env.OPENAI_API_KEY,
)
EMBEDEDING_MODEL = "text-embedding-3-large"
EMBEDEDING_DIM = 3072

splitter = SentenceSplitter()

def load_and_chunk_pdf(path: str) -> list[str]:
    docs = PDFReader().load_data(file=Path(path))
    texts = [doc.text for doc in docs if getattr(doc, "text", None)]
    chunks = []
    for text in texts:
        split_texts = splitter.split_text(text)
        chunks.extend(split_texts)
    return chunks
   
def embed_texts(texts: list[str]) -> list[list[float]]:
    responses = client.embeddings.create(
        input=texts,
        model=EMBEDEDING_MODEL
    )
    return [response.embedding for response in responses.data]