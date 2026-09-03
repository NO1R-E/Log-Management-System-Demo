import socket
import time
import random
from datetime import datetime

TARGET_HOST = "localhost"
TARGET_PORT = 5514

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# a few source/dest pairs to randomize, so the demo doesn't look static
SRC_IPS = ["10.0.1.10", "10.0.1.22", "10.0.2.5", "192.168.1.44"]
DST_IPS = ["8.8.8.8", "1.1.1.1", "8.8.4.4"]
ACTIONS = ["deny", "allow"]
PORTS = [53, 80, 443, 5353]

def build_syslog_line():
    pri = 134  # facility/severity encoded, matches the sample
    timestamp = datetime.utcnow().strftime("%b %d %H:%M:%S")
    src = random.choice(SRC_IPS)
    dst = random.choice(DST_IPS)
    action = random.choice(ACTIONS)
    spt = random.choice(PORTS)
    dpt = 53

    line = (
        f"<{pri}>{timestamp} fw01 vendor=demo product=ngfw "
        f"action={action} src={src} dst={dst} spt={spt} dpt={dpt} "
        f"proto=udp msg=DNS_blocked policy=Block-DNS"
    )
    return line

def send_one():
    line = build_syslog_line()
    sock.sendto(line.encode(), (TARGET_HOST, TARGET_PORT))
    print(f"Sent: {line}")

if __name__ == "__main__":
    print(f"Sending simulated firewall syslog to {TARGET_HOST}:{TARGET_PORT} (Ctrl+C to stop)\n")
    try:
        while True:
            send_one()
            time.sleep(random.uniform(1, 3))  # simulate irregular real traffic
    except KeyboardInterrupt:
        print("\nStopped.")