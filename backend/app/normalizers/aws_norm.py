def normalize_aws(raw: dict) -> dict:
    cloud = raw.get("cloud", {})
    inner = raw.get("raw", {})
    return {
        "tenant": raw["tenant"],
        "ts": raw["@timestamp"],
        "source": "aws",
        "event_type": raw.get("event_type") or inner.get("eventName"),
        "user": raw.get("user"),
        "cloud_account_id": cloud.get("account_id"),
        "cloud_region": cloud.get("region"),
        "cloud_service": cloud.get("service"),
        "raw": raw,
    }