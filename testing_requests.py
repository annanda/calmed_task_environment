import requests
from flask import json

data = {'mood': 'neutral', 'task': 'first_task'}
data_json = json.dumps(data)

r = requests.post('http://0.0.0.0:90/store_mood', json=data)
print(r.content)
