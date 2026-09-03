from app.db.connection import pool
from app.schemas.log import LogEntry

def save_log(entry: LogEntry, normalized: dict):
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO logs (tenant, ts, source, event_type, action,
                                   src_ip, dst_ip, "user", host,
                                   cloud_account_id, cloud_region, cloud_service, raw)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (entry.tenant, entry.ts, entry.source, entry.event_type,
                 entry.action, entry.src_ip, entry.dst_ip, entry.user, entry.host,
                 normalized.get("cloud_account_id"), normalized.get("cloud_region"),
                 normalized.get("cloud_service"), entry.model_dump_json())
            )
        conn.commit()