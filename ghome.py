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
#def wake_me_up_at(alarm_hr,alarm_min):
	# if for some reason this script is still running
# after a year, we'll stop after 365 days
def wake_me_up_at(hr,min):
	for i in xrange(0,365):
	    # sleep until 2AM
	    t = datetime.datetime.today() #today's info
	    future = datetime.datetime(t.year,t.month,t.day,hr,min) #alarm info
	    if t.hour >= hr:
	        future += datetime.timedelta(days=1)
	        print(future)
	        print("waiting. . .")
	    time.sleep((future-t).seconds)
		

	cast_start()



wake_me_up_at(6,0)



