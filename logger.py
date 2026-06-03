def log_result(message):
    with open("data/results.txt", "a") as f:
        f.write(message + "\n")