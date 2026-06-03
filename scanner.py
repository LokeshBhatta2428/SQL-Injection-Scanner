from concurrent.futures import ThreadPoolExecutor
import config
import payload
import requester
import detector
import auth
import logger


def scan_payload(session, payload_str):
    print(f"Testing: {payload_str}")

    try:
        response, elapsed = requester.send_request(session, payload_str)

        # Error-based detection
        if detector.error_based_detection(response.text):
            result = f"[!] Error-based SQLi detected: {payload_str}"
            print(result)
            logger.log_result(result)
        else:
            print(f"[-] No match for: {payload_str}")

        # Time-based detection
        if "SLEEP" in payload_str.upper() or "WAITFOR" in payload_str.upper():
            print(f"[*] Elapsed time: {elapsed:.2f}s")
            if detector.time_based_detection(elapsed):
                result = f"[!] Time-based SQLi detected: {payload_str}"
                print(result)
                logger.log_result(result)

    except Exception as e:
        print(f"Error testing payload '{payload_str}': {e}")


def main():
    print("=== SQL Injection Scanner ===")

    # Single login — reuse same session for all payloads
    try:
        session = auth.login()
        print("[+] Logged into DVWA successfully")
    except Exception as e:
        print(e)
        return

    # Load payloads
    all_payloads = payload.load_payloads()
    print(f"[+] Loaded {len(all_payloads)} payloads")

    # Multithreading — pass the same session
    with ThreadPoolExecutor(max_workers=config.THREADS) as executor:
        for p in all_payloads:
            executor.submit(scan_payload, session, p)

    print("[+] Scan complete. Results saved to datafiles/results.txt")


if __name__ == "__main__":
    main()