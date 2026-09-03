def normalize_ad(raw: dict) -> dict:
    return {
        "tenant": raw["tenant"],
        "ts": raw["@timestamp"],
        "source": "ad",
        "event_type": raw.get("event_type"),
        "user": raw.get("user"),
        "host": raw.get("host"),
        "src_ip": raw.get("ip"),
        "action": "login" if raw.get("event_id") == 4624 else "deny",
        "raw": raw,
    }