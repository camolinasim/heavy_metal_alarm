import requests
import json


def cast_start():
	payload = {
	    "device": "Eril Display", 
	    "source": "https://www.youtube.com/watch?time_continue=11&v=XdiGdC7K4sI&feature=emb_logo",
	    "type": "remote"
	}
	r = requests.post('http://ar.local:3000/cast/', json=payload)

	print("Status code: ", r.status_code)
	print("Printing Entire Post Request")
	#print(r)
	print(r.text)

def cast_stop():
	payload = {
        "device": "Eril Display",
        "force": True
}
	r = requests.post('http://ar.local:3000/cast/', json=payload)

	print("Status code: ", r.status_code)
	print("Printing Entire Post Request")
	#print(r)
	print(r.text)

cast_start()
