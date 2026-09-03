def normalize_api(raw: dict) -> dict:
    return {
        "tenant": raw["tenant"],
        "ts": raw["@timestamp"],
        "source": "api",
        "event_type": raw.get("event_type"),
        "user": raw.get("user"),
        "src_ip": raw.get("ip"),
        "raw": raw,
    }