import requests
import datetime
import time

video = "https://www.youtube.com/watch?v=mshYP5KgzOY"


def cast_to(device_name):
    payload = {
        "device": str(device_name),
        "source": video,
        "type": "remote"
    }
    print("trying to cast...")

    r = requests.post('http://ar.local:3000/cast/', json=payload)

    print("Status code: ", r.status_code)
    if(r.status_code != 200):
        knock_door_three_times(payload)
    print(r.text)


def cast_stop():
    payload = {
        "device": "Elric Brothers",
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
def wake_me_up_at(hr, min, sec):
    # sleep until 2AM
    t = datetime.datetime.today()  # today's info
    future = datetime.datetime(
        t.year, t.month, t.day, hr, min, sec)  # alarm info
    if t.hour >= hr:
        future += datetime.timedelta(days=0)
        print(future)
        print("waiting. . .")
        time.sleep((future - t).seconds)
        cast_to("Eril Display")


def knock_door_three_times(payload):
    knock_door(payload)
    knock_door(payload)
    knock_door(payload)


def knock_door(payload):
    requests.post('http://ar.local:3000/cast/', json=payload)
    time.sleep(3)


def clear():
    print('\n' * 100)
clear()
wake_me_up_at(14, 59, 50)
# cast_to("Eril Display")

# cast_stop()
