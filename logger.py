import os
from datetime import datetime


def log_result(message):
    os.makedirs("datafiles", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("datafiles/results.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")