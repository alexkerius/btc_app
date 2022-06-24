import requests
import itertools

secret_key="eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6InF1OXA1NC0wMCIsInVzZXJfaWQiOiI3OTAzNzk1NDU0MyIsInNlY3JldCI6IjZhMTM3ZGI4M2NkYjU3OTUxOWFhMzM2Yzk3ODRiNGJmYjYwMTg0OGNlYjBiZWI3YzE2YmEzMzQ5ZTI5YjVjYjIifX0="
billid="25341703463"
headers={"Authorization":f"Bearer {secret_key}",
"Accept":"application/json"}
url=f"https://api.qiwi.com/partner/bill/v1/bills/{billid}"
#r=requests.get(url=url,headers=headers).json()
print(dict(itertools.islice(headers.items(),2)))