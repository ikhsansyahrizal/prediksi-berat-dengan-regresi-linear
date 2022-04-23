import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Height':169, 'Gender':1})

print(r.json())