from concurrent.futures import ThreadPoolExecutor
import config
import payload
import requester
import detector
import auth
import logger


def scan_payload(payload_str):
    """Each thread creates its own session to avoid thread-safety issues."""
    session = auth.login()
    print(f"Testing: {payload_str}")

    try:
        response, elapsed = requester.send_request(session, payload_str)

        # Error-based detection
        if detector.error_based_detection(response.text):
            result = f"[!] Error-based SQLi detected: {payload_str}"
            print(result)
            logger.log_result(result)

        # Time-based detection
        if "SLEEP" in payload_str.upper():
            if detector.time_based_detection(elapsed):
                result = f"[!] Time-based SQLi detected: {payload_str}"
                print(result)
                logger.log_result(result)

    except Exception as e:
        print(f"Error testing payload '{payload_str}': {e}")


def main():
    print("=== SQL Injection Scanner ===")

    # Verify login works before launching threads
    try:
        auth.login()
        print("[+] Logged into DVWA successfully")
    except Exception as e:
        print(e)
        return

    # Load payloads
    all_payloads = payload.load_payloads()
    print(f"[+] Loaded {len(all_payloads)} payloads")

    # Multithreading — each thread handles its own session
    with ThreadPoolExecutor(max_workers=config.THREADS) as executor:
        for p in all_payloads:
            executor.submit(scan_payload, p)

    print("[+] Scan complete. Results saved to datafiles/results.txt")


if __name__ == "__main__":
    main()