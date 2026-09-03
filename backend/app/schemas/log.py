from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID

class LogEntry(BaseModel):
    tenant: str
    ts: datetime = Field(alias="@timestamp")
    source: str
    vendor: Optional[str] = None
    product: Optional[str] = None
    event_type: Optional[str] = None
    event_subtype: Optional[str] = None
    severity: Optional[int] = None
    action: Optional[str] = None
    src_ip: Optional[str] = None
    src_port: Optional[int] = None
    dst_ip: Optional[str] = None
    dst_port: Optional[int] = None
    protocol: Optional[str] = None
    user: Optional[str] = None
    host: Optional[str] = None
    process: Optional[str] = None
    url: Optional[str] = None
    http_method: Optional[str] = None
    status_code: Optional[int] = None
    rule_name: Optional[str] = None
    rule_id: Optional[str] = None
    raw: dict = Field(default_factory=dict)

    class Config:
        populate_by_name = True