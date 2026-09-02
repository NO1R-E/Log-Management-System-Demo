from fastapi import FastAPI
from app.core.database import get_connection
from app.core.config import settings

app = FastAPI(title="Log Management System")

# print("DB URL in use:", settings.database_url)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/health/db")
def health_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
            return {"db": cur.fetchone()[0] == 1}