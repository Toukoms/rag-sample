from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import os

class QdrantStorage:
  def __init__(self, url=os.getenv("QDRANT_URL", "http://localhost:6333"), collection_name="docs", dim=3072):
    self.client = QdrantClient(url=url)
    self.collection_name = collection_name

    # Create collection if it doesn't exist
    if not self.client.collection_exists (collection_name):
      self.client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=dim, distance=Distance.COSINE)
      )
      
  def upsert_vectors(self, ids, vectors, payloads):
    points = [
      PointStruct(id=id, vector=vector, payload=payload)
      for id, vector, payload in zip(ids, vectors, payloads)
    ]
    self.client.upsert(
      collection_name=self.collection_name,
      points=points
    )
    
  def search_vectors(self, query_vector, limit=5):
    results = self.client.query_points(
      collection_name=self.collection_name,
      query=query_vector,
      limit=limit
    )
    contexts = []
    sources = set()
    
    for result in results:
      payload = getattr(result, 'payload', {})
      text = payload.get('text', '')
      source = payload.get('source', '')
      if text:
        contexts.append(text)
        if source:
          sources.add(source)  
          
    return { "contexts": contexts, "sources": list(sources) }  
  
    
  