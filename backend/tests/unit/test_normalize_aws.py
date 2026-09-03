from app.normalizers.aws_norm import normalize_aws

def test_normalize_aws_basic_fields():
    raw = {
        "tenant": "demoB",
        "source": "aws",
        "cloud": {"service": "iam", "account_id": "123456789012", "region": "ap-southeast-1"},
        "event_type": "CreateUser",
        "user": "admin",
        "@timestamp": "2025-08-20T09:10:00Z",
        "raw": {"eventName": "CreateUser", "requestParameters": {"userName": "temp-user"}}
    }

    result = normalize_aws(raw)

    assert result["tenant"] == "demoB"
    assert result["source"] == "aws"
    assert result["event_type"] == "CreateUser"
    assert result["user"] == "admin"
    assert result["cloud_account_id"] == "123456789012"
    assert result["cloud_region"] == "ap-southeast-1"
    assert result["cloud_service"] == "iam"

def test_normalize_aws_falls_back_to_raw_event_name():
    # event_type missing at top level, should pull from raw.eventName instead
    raw = {
        "tenant": "demoB",
        "source": "aws",
        "cloud": {"service": "iam", "account_id": "123", "region": "us-east-1"},
        "@timestamp": "2025-08-20T09:10:00Z",
        "raw": {"eventName": "DeleteUser"}
    }

    result = normalize_aws(raw)

    assert result["event_type"] == "DeleteUser"