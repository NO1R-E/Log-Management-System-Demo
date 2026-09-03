def normalize_m365(raw: dict) -> dict:
    return {
        "tenant": raw["tenant"],
        "ts": raw["@timestamp"],
        "source": "m365",
        "event_type": raw.get("event_type"),
        "user": raw.get("user"),
        "src_ip": raw.get("ip"),
        "action": "login" if raw.get("status") == "Success" else "deny",
        "raw": raw,
    }