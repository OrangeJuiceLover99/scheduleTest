from datetime import datetime

with open("output.txt", "a") as f:
    f.write(f"Script lief am {datetime.now()}\n")

print("Script wurde ausgeführt!")
