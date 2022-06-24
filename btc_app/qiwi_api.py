import requests
import json
import datetime


def qiwi_api_function():
    billid="da8d9adw89a-adjw1jidja-2a9d9s-2jdsji"
    secret_key="eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6ImV2OXJ1NS0wMCIsInVzZXJfaWQiOiI3OTY4NzI3MDc1OSIsInNlY3JldCI6ImU5MGYxNTk2MTAwNWYzM2M0M2Q5OGMyM2MzZGM5MjU0YjMzYzJhZTE3M2RhOGFmNGM1YjhiZWVmYjliNmNhYTIifX0="
    url=f"https://api.qiwi.com/partner/bill/v1/bills/{billid}"
    headers={"Authorization":f"Bearer {secret_key}",
    "Content-Type": "application/json",
    "Accept": "application/json"}
    parameters={"amount":
    {"value":get_entered_amount(),
    "currency":"RUB"},
    "expirationDateTime":"2022-06-17T2:00:00+03:00"}
    r=requests.put(url=url,json=parameters,headers=headers).text
    print(json.loads(r))
hour=1
#date=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S+03:00")
date=datetime.datetime.now()
added=datetime.timedelta(hours=hour)
expirationdate=date+added
expirationdate=expirationdate.strftime("%Y-%m-%dT%H:%M:%S+03:00")
print(expirationdate)

    