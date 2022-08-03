import requests

payload = {
    "ip1" : "192.168.4.0/23",
    "ip2" : "192.168.4.0/22"
}

url = "http://127.0.0.1:8000/v1/check-ip"

r = requests.post(url, params=payload)
# print(type(r))
r = r.content
# r = r.decode('utf-8')
print(r)

# uvicorn main:app --reload