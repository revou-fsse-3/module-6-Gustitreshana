import requests

ENDPOINT = "https://documenter.getpostman.com/view/29213022/2sA2r9VNm7"

response = requests.get(ENDPOINT)
print(response)
