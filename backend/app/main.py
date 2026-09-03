from fastapi import FastAPI
from app.config import settings
from app.api.ingest import router as ingest_router
from app.api.search import router as search_router
from app.api.status import router as status_router

app = FastAPI(title="Log Management System")

# print("DB URL in use:", settings.database_url)
app.include_router(status_router)
app.include_router(ingest_router)
app.include_router(search_router)