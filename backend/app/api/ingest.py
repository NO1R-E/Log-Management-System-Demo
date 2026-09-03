from fastapi import APIRouter, Request, HTTPException
from app.schemas.log import LogEntry
from app.normalizers import NORMALIZERS
from app.core.log_writer import save_log

router = APIRouter()

@router.post("/ingest")
async def ingest_log(request: Request):
    raw = await request.json()
    source = raw.get("source")

    normalizer = NORMALIZERS.get(source)
    if not normalizer:
        raise HTTPException(status_code=400, detail=f"Unknown source: {source}")

    normalized = normalizer(raw)
    entry = LogEntry(**normalized)
    save_log(entry, normalized)
    return {"status": "stored"}