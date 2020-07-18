import requests
import datetime
import time
from multiprocessing import Process, current_process

# represents the media to be casted to google devices
video = "https://www.youtube.com/watch?v=9n-yiNx8sbY"
shia = "https://www.youtube.com/watch?v=qX1PvJfpbc4"

# Asks the name of the device to cast to and the media to send.
# In the case of failing to connect, it will try reconnecting three more times.
# If that fails, a connectionError exception is raised"""


def cast_to(device_name, media):

    payload = {
        "device": str(device_name),
        "source": media,
        "type": "remote"
    }

    print(f"trying to cast to {device_name}.")

    r = requests.post('http://ar.local:3000/cast/', json=payload)

    print("Status code: ", r.status_code)
    if(r.status_code != 200):
        knock_door_three_times(payload)
    print(r.text)


# stops a current casting session
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


# Asks for the time you want woken up and plays the video from cast_start
# method at the specified time
def wake_me_up_at(hr, min, sec):
    # get today's date and time
    today = datetime.datetime.today()

    # get when the date and time of the alarm
    alarm_time = datetime.datetime(
        today.year, today.month, today.day, hr, min, sec)

    # alarm logic
    if today.hour >= hr:
        alarm_time += datetime.timedelta(days=0)
        print("waiting until " + str(alarm_time) + ". . .")
        time.sleep((alarm_time - today).seconds)

    # Cast when alarm time
        cast_to("Eril Display", media)


# Helper method for cast_to function. Big Idea: if the first cast attempt
# fails, let's try it three more times
def knock_door_three_times(payload):
    knock_door(payload)
    knock_door(payload)
    knock_door(payload)


# Helper method for knock_three_times function
def knock_door(payload):
    requests.post('http://ar.local:3000/cast/', json=payload)
    time.sleep(3)


def synchronize():

    processes = []
    inputs = ["Eril Display", "Eril TV"]
    media = [video, shia]
    media_counter = 0

    for inp in inputs:
        print(media_counter)
        print(media[media_counter])
        process = Process(target=cast_to, args=(inp, media[media_counter]))
        media_counter += 1
        processes.append(process)

        process.start()
        process.join()

synchronize()
# wake_me_up_at(6, 0, 0)
# cast_to("Eril Display", video)
# cast_to("Eril TV", video)

time.sleep(12)
cast_stop()
