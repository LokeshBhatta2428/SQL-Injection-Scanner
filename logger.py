def log_result(message):
    with open("datafiles/results.txt", "a") as f:
        f.write(message + "\n")