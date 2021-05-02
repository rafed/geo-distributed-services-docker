import requests
import time

url = "http://dhaka.server.com"

for i in range(1000):
    if i%2 == 0:
        r = requests.get(f"{url}/api/v1/{i}")
    else:
        r = requests.get(f"{url}/api/v2/{i}")

    print(r.text)
    time.sleep(1)
