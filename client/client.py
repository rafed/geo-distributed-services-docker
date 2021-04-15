import requests
import time

for i in range(1000):
    if i%2 == 0:
        r = requests.get(f"http://localhost:8080/api/v1/{i}")
    else:
        r = requests.get(f"http://localhost:8080/api/v2/{i}")

    print(r.text)
    time.sleep(1)