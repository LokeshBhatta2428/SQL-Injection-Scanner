import requests
import config

def login():
    session = requests.Session()

    login_data = {
        "username": config.USERNAME,
        "password": config.PASSWORD,
        "Login": "Login"
    }

    session.post(config.LOGIN_URL, data=login_data)
    return session