import requests
import config


def login():
    session = requests.Session()

    login_data = {
        "username": config.USERNAME,
        "password": config.PASSWORD,
        "Login": "Login"
    }

    response = session.post(config.LOGIN_URL, data=login_data)

    # Verify login succeeded
    if "Login failed" in response.text or response.status_code != 200:
        raise Exception("[-] Login failed! Check credentials or DVWA URL.")

    # Set DVWA security level cookie
    session.cookies.set("security", config.SECURITY_LEVEL)

    return session