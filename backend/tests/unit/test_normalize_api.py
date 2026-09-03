from app.normalizers.api_norm import normalize_api

def test_normalize_api_login_failed():
    raw = {
        "tenant": "demoA",
        "source": "api",
        "event_type": "app_login_failed",
        "user": "alice",
        "ip": "203.0.113.7",
        "reason": "wrong_password",
        "@timestamp": "2025-08-20T07:20:00Z"
    }

    result = normalize_api(raw)

    assert result["tenant"] == "demoA"
    assert result["event_type"] == "app_login_failed"
    assert result["src_ip"] == "203.0.113.7"