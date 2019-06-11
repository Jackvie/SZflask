import requests,json

url = "http://127.0.0.1:5000/"
#url += "hello/13"
url += "register/11111111111"

response = requests.get(url)
ret = response.content.decode()
print(ret)





