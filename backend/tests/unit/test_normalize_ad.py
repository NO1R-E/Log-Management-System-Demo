from app.normalizers.ad_norm import normalize_ad

def test_normalize_ad_failed_logon():
    raw = {
        "tenant": "demoA",
        "source": "ad",
        "event_id": 4625,
        "event_type": "LogonFailed",
        "user": "demo\\eve",
        "host": "DC01",
        "ip": "203.0.113.77",
        "logon_type": 3,
        "@timestamp": "2025-08-20T11:11:11Z"
    }

    result = normalize_ad(raw)

    assert result["source"] == "ad"
    assert result["action"] == "deny"          # 4625 = failed logon
    assert result["src_ip"] == "203.0.113.77"
    assert result["host"] == "DC01"

def test_normalize_ad_successful_logon():
    raw = {
        "tenant": "demoA", "source": "ad", "event_id": 4624,
        "event_type": "LogonSuccess", "user": "demo\\alice",
        "host": "DC01", "ip": "203.0.113.10",
        "@timestamp": "2025-08-20T11:12:00Z"
    }

    result = normalize_ad(raw)

    assert result["action"] == "login"         # 4624 = successful logon