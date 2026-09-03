from app.normalizers.syslog_norm import parse_syslog_line

def test_parse_syslog_line_extracts_fields():
    line = "<134>Aug 20 12:44:56 fw01 vendor=demo product=ngfw action=deny src=10.0.1.10 dst=8.8.8.8 spt=5353 dpt=53 proto=udp"
    result = parse_syslog_line(line)

    assert result["pri"] == 134
    assert result["host"] == "fw01"
    assert result["action"] == "deny"
    assert result["src"] == "10.0.1.10"