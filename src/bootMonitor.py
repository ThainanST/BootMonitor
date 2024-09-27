import os
import datetime

def register_boot():
    log_file = "boot_log.txt"
    
    # now = datetime.datetime.now()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a") as f:
        f.write(f"{now}\n")

if __name__ == "__main__":
    register_boot()