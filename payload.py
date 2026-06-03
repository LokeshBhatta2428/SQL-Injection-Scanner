def load_payloads():
    with open("data/payloads.txt", "r") as f:
        return f.read().splitlines()