def load_payloads():
    with open("datafiles/payloads.txt", "r") as f:
        return f.read().splitlines()