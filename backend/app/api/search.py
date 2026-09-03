from fastapi import APIRouter, Query
from datetime import datetime
from typing import Optional
from app.db.connection import pool

router = APIRouter()

@router.get("/logs")
def search_logs(
    tenant: str = Query(..., description="Required - tenant to scope results to"),
    source: Optional[str] = Query(None),
    event_type: Optional[str] = Query(None),
    src_ip: Optional[str] = Query(None),
    user: Optional[str] = Query(None),
    start: Optional[datetime] = Query(None),
    end: Optional[datetime] = Query(None),
    limit: int = Query(50, le=500),
    offset: int = Query(0, ge=0),
):
    conditions = ["tenant = %s"]
    params = [tenant]

    if source:
        conditions.append("source = %s")
        params.append(source)
    if event_type:
        conditions.append("event_type = %s")
        params.append(event_type)
    if src_ip:
        conditions.append("src_ip = %s")
        params.append(src_ip)
    if user:
        conditions.append('"user" = %s')
        params.append(user)
    if start:
        conditions.append("ts >= %s")
        params.append(start)
    if end:
        conditions.append("ts <= %s")
        params.append(end)

    where_clause = " AND ".join(conditions)
    query = f"""
        SELECT tenant, ts, source, event_type, action, src_ip, dst_ip, "user", host, raw
        FROM logs
        WHERE {where_clause}
        ORDER BY ts DESC
        LIMIT %s OFFSET %s
    """
    params.extend([limit, offset])

    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            columns = [desc[0] for desc in cur.description]
            rows = cur.fetchall()

    return {
        "results": [dict(zip(columns, row)) for row in rows],
        "count": len(rows),
        "limit": limit,
        "offset": offset,
    }