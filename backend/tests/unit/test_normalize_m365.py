from app.normalizers.m365_norm import normalize_m365

def test_normalize_m365_successful_login():
    raw = {
        "tenant": "demoB",
        "source": "m365",
        "event_type": "UserLoggedIn",
        "user": "bob@demo.local",
        "ip": "198.51.100.23",
        "status": "Success",
        "workload": "Exchange",
        "@timestamp": "2025-08-20T10:05:00Z"
    }

    result = normalize_m365(raw)

    assert result["tenant"] == "demoB"
    assert result["source"] == "m365"
    assert result["event_type"] == "UserLoggedIn"
    assert result["user"] == "bob@demo.local"
    assert result["src_ip"] == "198.51.100.23"
    assert result["action"] == "login"

def test_normalize_m365_failed_login():
    raw = {
        "tenant": "demoB",
        "source": "m365",
        "event_type": "UserLoginFailed",
        "user": "eve@demo.local",
        "ip": "198.51.100.99",
        "status": "Failed",
        "workload": "Exchange",
        "@timestamp": "2025-08-20T10:06:00Z"
    }

    result = normalize_m365(raw)

    assert result["action"] == "deny"