import re
from datetime import datetime

SYSLOG_PATTERN = re.compile(
    r"<(?P<pri>\d+)>(?P<timestamp>\w+ +\d+ \d+:\d+:\d+) (?P<host>\S+) (?P<message>.*)"
)

def parse_syslog_line(line: str) -> dict:
    match = SYSLOG_PATTERN.match(line)
    if not match:
        return {"raw_unparsed": line}

    parts = match.groupdict()

    # pull out key=value pairs from the free-form message, if present
    kv_pairs = dict(re.findall(r"(\w+)=(\S+)", parts["message"]))

    return {
        "pri": int(parts["pri"]),
        "host": parts["host"],
        "message": parts["message"],
        **kv_pairs,   # e.g. src, dst, action, proto all land here
    }

def normalize_syslog(raw_line: str, tenant: str = "demoA") -> dict:
    parsed = parse_syslog_line(raw_line)
    return {
        "tenant": tenant,
        "ts": datetime.utcnow().isoformat(),  # syslog timestamps lack year/tz, using receive time is simplest for now
        "source": "syslog",
        "action": parsed.get("action"),
        "src_ip": parsed.get("src"),
        "dst_ip": parsed.get("dst"),
        "protocol": parsed.get("proto"),
        "raw": {"line": raw_line, "parsed": parsed},
    }