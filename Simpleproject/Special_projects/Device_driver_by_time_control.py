from datetime import datetime
from subprocess import run
from time import sleep

while True:
    now = datetime.now()
    time_string = now.strftime("%H:%M:%S")
    hours = int(time_string[:2])

    if hours>=20 or hours<=8:
        run(["shutdown", "/s", "/t", "0"])

    sleep(500)
