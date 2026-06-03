# Configuration settings

BASE_URL = "http://localhost/dvwa/vulnerabilities/sqli/"
LOGIN_URL = "http://localhost/dvwa/login.php"

USERNAME = "admin"
PASSWORD = "password"

SECURITY_LEVEL = "low"  # DVWA security level cookie

THREADS = 5
DELAY = 1
TIMEOUT = 10  # slightly higher to accommodate time-based payloads

ERROR_PATTERNS = [
    "SQL syntax",
    "mysql",
    "ORA-",
    "syntax error",
    "unexpected"
]