import config


def error_based_detection(response_text):
    for error in config.ERROR_PATTERNS:
        if error.lower() in response_text.lower():
            return True
    return False


def time_based_detection(elapsed):
    """Check if response took longer than 4 seconds (indicates SLEEP payload worked)."""
    return elapsed > 4

