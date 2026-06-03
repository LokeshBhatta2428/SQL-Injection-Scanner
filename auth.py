import requests
from bs4 import BeautifulSoup
import config


def get_csrf_token(session, url):
    """Grab the user_token from the login page."""
    response = session.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    token = soup.find("input", {"name": "user_token"})
    if token:
        return token["value"]
    return None


def login():
    session = requests.Session()

    # Get login page + CSRF token
    token = get_csrf_token(session, config.LOGIN_URL)

    login_data = {
        "username": config.USERNAME,
        "password": config.PASSWORD,
        "Login": "Login"
    }

    # Add token if present
    if token:
        login_data["user_token"] = token
        print(f"[DEBUG] CSRF token found: {token[:10]}...")
    else:
        print("[DEBUG] No CSRF token found, proceeding without it")

    response = session.post(config.LOGIN_URL, data=login_data, allow_redirects=True)

    print(f"[DEBUG] Final URL after login: {response.url}")

    # Set DVWA security level cookie
    session.cookies.set("security", config.SECURITY_LEVEL)

    return session