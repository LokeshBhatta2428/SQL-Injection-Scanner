import time
import config

def send_request(session, payload):
    params = {
        "id": "1" + payload,
        "Submit": "Submit"
    }

    response = session.get(config.BASE_URL, params=params, timeout=config.TIMEOUT)
    
    time.sleep(config.DELAY)  # rate limiting

    return response