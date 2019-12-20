import requests




response = requests.get('http://127.0.0.1:8000/api/')
# print(response.status_code)
# print(response.encoding)
# print(response.url)
# str1 = response.text
# print(str1)
# print(type(str1))
print(response.json())

