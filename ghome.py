import requests
import json
import datetime
import time


def cast_start():
	payload = {
	    "device": "Eril Display", 
	    "source": "https://www.youtube.com/watch?v=mshYP5KgzOY",
	    "type": "remote"
	}
	r = requests.post('http://ar.local:3000/cast/', json=payload)

	print("Status code: ", r.status_code)
	print("Printing Entire Post Request")
	#print(r)
	print(r.text)

#Asks for the time you want woken up and plays the video from cast_start method
#at the specified time
def wake_me_up_at(hr,min,sec):
	now = datetime.datetime.now()
	alarm_time = datetime.datetime.combine(now.date(), datetime.time(hr, min,sec))
	time.sleep((alarm_time - now).total_seconds())
	cast_start()

wake_me_up_at(9,49,20)



