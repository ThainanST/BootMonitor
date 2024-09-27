import os
import datetime

def update_file():
    with open("src/boot_log.txt", "a") as f:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{now}\n")

def commit_and_push():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.system("git add .")
    os.system(f'git commit -m "Automatic update on {current_time}"')
    os.system("git push origin main")

if __name__ == "__main__":
    update_file()
    commit_and_push()