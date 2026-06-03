def load_payloads():
    try:
        with open("datafiles/payloads.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        raise FileNotFoundError("[-] payloads.txt not found in datafiles/")