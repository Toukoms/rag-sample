from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

class Env(BaseModel):
    OPENAI_API_BASE_URL: str
    OPENAI_API_KEY: str
    ENV: str = "development"
    QDRANT_URL: str
    INNGEST_API_BASE: str = "http://localhost:8288/v1"
    MAIN_MODEL: str
    EMBEDDING_MODEL: str
    EMBEDDING_DIM: int = 3072
    COLLECTION_NAME: str = "docs"
    
env = Env.model_validate(os.environ)
    