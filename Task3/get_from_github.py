#!/usr/bin/env python3
import base64
import requests


url = 'https://api.github.com/repos/Abhi135721/caravel-interview/contents/Task2/quiz.py'
req = requests.get(url)
print(req)
if req.status_code == requests.codes.ok:
	res = req.json()  # the response is a JSON
	# req is now a dict with keys: name, encoding, url, size ...
	# and content. But it is encoded with base64.
	content = base64.b64decode(res['content']).decode("UTF-8")
else:
    print('Content was not found.')
	
with open("C:\\Users\\abhia\\Desktop\\New Folder\\caravel-interview\\Task3\\quiz.py" , "w") as f:
	f.write(content)
f.close()




