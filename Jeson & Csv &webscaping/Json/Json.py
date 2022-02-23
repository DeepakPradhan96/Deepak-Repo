import requests
import json
import jsonpath

url='https://reqres.in/api/users?page=2'

# Send Get_Request
respons1=requests.get(url)
print(respons1.text)

#validate Response Status Code of url
assert respons1.status_code==200
print('greet')

# Convert Response Intu Json Format

json=json.loads(respons1.text)
print(json)

#apply Json path
jsonpath=jsonpath.jsonpath(json,'data[2].email')
print(jsonpath[0])

'''for i in json['data']:
    print(i['email'])'''