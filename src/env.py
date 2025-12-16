import pydantic
import os

class Env(pydantic.BaseModel):
    OPENAI_API_BASE_URL: str
    OPENAI_API_KEY: str
    ENV: str
    QDRANT_URL: str
    
env = Env.model_validate(os.environ)
    