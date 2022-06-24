import requests
from json import dumps
webhook_url="http://127.0.0.1:5000"

data={"First name":"Alex",
"Last name":"Kitaev"}

r=requests.post(webhook_url,data=dumps(data),headers={"Content-Type":"application/json"})
