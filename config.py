# Configuration settings

BASE_URL = "http://localhost/dvwa/vulnerabilities/sqli/"
LOGIN_URL = "http://localhost/dvwa/login.php"

USERNAME = "admin"
PASSWORD = "password"

THREADS = 5
DELAY = 1
TIMEOUT = 5

ERROR_PATTERNS = [
    "SQL syntax",
    "mysql",
    "ORA-",
    "syntax error",
    "unexpected"
]