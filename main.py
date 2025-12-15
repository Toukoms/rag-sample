import logging
from fastapi import FastAPI
from dotenv import load_dotenv
import os
import inngest
import uuid
import datetime
from inngest.experimental import ai

load_dotenv()

inngest_client = inngest.Inngest(
  app_id="rag_app",
  logger=logging.getLogger("uvicorn"),
  isProduction=os.getenv("ENV") == "production",
  serializer=inngest.PydanticSerializer()
)

app = FastAPI()

inngest.fastapi.setup(app, inngest_client, [])

