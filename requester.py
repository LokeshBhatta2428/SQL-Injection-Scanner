import time
import config


def send_request(session, payload):
    params = {
        "id": "1" + payload,
        "Submit": "Submit"
    }

    start = time.time()
    response = session.get(config.BASE_URL, params=params, timeout=config.TIMEOUT)
    elapsed = time.time() - start

    time.sleep(config.DELAY)  # rate limiting

    return response, elapsed