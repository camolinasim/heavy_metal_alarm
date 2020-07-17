import requests
import datetime
import time


def cast_start():
    payload = {
        "device": "Elric Brothers",
        "source": "https://www.youtube.com/watch?v=mshYP5KgzOY",
        "type": "remote"
    }
    r = requests.post('http://ar.local:3000/cast/', json=payload)

    print("Status code: ", r.status_code)
    print("Attempting to cast")
    # print(r)
    print(r.text)


def cast_stop():
    payload = {
        "device": "Eril Display",
        "force": True
    }
    print("attempting to stop cast")
    r = requests.post('http://ar.local:3000/cast/stop', json=payload)

    print("Status code: ", r.status_code)
    # print(r)
    print(r.text)


# Asks for the time you want woken up and plays the video from cast_start method
# at the specified time
# if for some reason this script is still running
# after a year, we'll stop after 365 days
def wake_me_up_at(hr, min):
    for i in range(0, 365):
        # sleep until 2AM
        t = datetime.datetime.today()  # today's info
        future = datetime.datetime(
            t.year, t.month, t.day, hr, min)  # alarm info
        if t.hour >= hr:
            future += datetime.timedelta(days=1)
            print(future)
            print("waiting. . .")
        time.sleep((future - t).seconds)
        print("trying to cast...")

    cast_start()

cast_start()
