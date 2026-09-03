from app.normalizers.syslog_norm import normalize_syslog
from app.schemas.log import LogEntry
from app.core.log_writer import save_log

def handle_received_line(raw_line: str):
    normalized = normalize_syslog(raw_line)
    entry = LogEntry(**normalized)
    save_log(entry, normalized)