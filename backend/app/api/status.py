from fastapi import APIRouter, HTTPException, status
from app.db.connection import pool

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/health/db")
def health_db():
    try:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                result = cur.fetchone()
        return {"status": "healthy", "db": result[0] == 1 if result else False}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"status": "unhealthy", "database": "disconnected", "error": str(e)}
        )