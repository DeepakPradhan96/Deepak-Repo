import requests

#Sending Request with url

Url='https://heymates.me/a'
x=requests.get(Url)

#print('status code is :-',x.status_code)
#rint(x.text)

f=open('D:\\Result.txt','wb')

for data in x.iter_content(20000):
    f.write(data)

f.close()