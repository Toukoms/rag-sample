from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

class Env(BaseModel):
    OPENAI_API_BASE_URL: str
    OPENAI_API_KEY: str
    ENV: str
    QDRANT_URL: str
    
env = Env.model_validate(os.environ)
    