from concurrent.futures import ThreadPoolExecutor
import config
import payloads
import requester
import detector
import auth
import logger


def scan_payload(session, payload):
    print(f"Testing: {payload}")

    try:
        response = requester.send_request(session, payload)

        # Error-based detection
        if detector.error_based_detection(response.text):
            result = f"[!] Error-based SQLi detected: {payload}"
            print(result)
            logger.log_result(result)

        # Time-based detection
        if "SLEEP" in payload.upper():
            if detector.time_based_detection(session, payload):
                result = f"[!] Time-based SQLi detected: {payload}"
                print(result)
                logger.log_result(result)

    except Exception as e:
        print(f"Error: {e}")


def main():
    print("=== SQL Injection Scanner ===")

    # Login
    session = auth.login()
    print("[+] Logged into DVWA")

    # Load payloads
    all_payloads = payloads.load_payloads()

    # Multithreading
    with ThreadPoolExecutor(max_workers=config.THREADS) as executor:
        for payload in all_payloads:
            executor.submit(scan_payload, session, payload)


if __name__ == "__main__":
    main()