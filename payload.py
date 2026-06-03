def load_payloads():
    try:
        with open("datafiles/payloads.txt", "r") as f:
            # strip() removes \r\n on Windows and filters blank lines
            return [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError("[-] payloads.txt not found in datafiles/")