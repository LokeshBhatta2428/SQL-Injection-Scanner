import config
import time

def error_based_detection(response_text):
    for error in config.ERROR_PATTERNS:
        if error.lower() in response_text.lower():
            return True
    return False


def time_based_detection(session, payload):
    params = {
        "id": "1" + payload,
        "Submit": "Submit"
    }

    start = time.time()
    session.get(config.BASE_URL, params=params)
    end = time.time()

    if end - start > 4:
        return True

    return False