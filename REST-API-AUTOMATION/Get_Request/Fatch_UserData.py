import requests

url='https://reqres.in/api/users?page=2'

# Send Get_Request

response=requests.get(url)
#Display Response Content

print(response.content)
#print(response.text)

assert response.status_code==200 ,"Not Match"

#fatch response headers
print(response.headers)
print(response.headers.get("Date"))
print(response.headers.get("Age"))

#Fatch Cookies
print(response.cookies)

#fatch response.encoding
print(response.encoding)

print(response.elapsed)