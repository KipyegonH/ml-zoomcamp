import requests

url = "http://localhost:9696/score"

client = {"job": "student", "duration": 280, "poutcome": "failure"}
response = requests.post(url,json=client).json()
print(response)

if response['score']==True:
    print('sending promo email')
else:
    print('not sending promo email')