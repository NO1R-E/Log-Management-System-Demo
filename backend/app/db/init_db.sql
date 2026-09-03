CREATE TABLE IF NOT EXISTS logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant TEXT NOT NULL,
    ts TIMESTAMPTZ NOT NULL,
    source TEXT NOT NULL,
    vendor TEXT,
    product TEXT,
    event_type TEXT,
    event_subtype TEXT,
    severity SMALLINT,
    action TEXT,
    src_ip INET,
    src_port INT,
    dst_ip INET,
    dst_port INT,
    protocol TEXT,
    "user" TEXT,
    host TEXT,
    process TEXT,
    url TEXT,
    http_method TEXT,
    status_code INT,
    rule_name TEXT,
    rule_id TEXT,
    cloud_account_id TEXT,
    cloud_region TEXT,
    cloud_service TEXT,
    raw JSONB NOT NULL,
    tags TEXT[]
);

CREATE INDEX IF NOT EXISTS idx_logs_tenant_ts ON logs (tenant, ts DESC);
CREATE INDEX IF NOT EXISTS idx_logs_source ON logs (source);
CREATE INDEX IF NOT EXISTS idx_logs_raw ON logs USING GIN (raw);