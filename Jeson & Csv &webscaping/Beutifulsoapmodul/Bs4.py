import bs4
import requests

#Sending Request with url

Url='https://heymates.me/a'
respons=requests.get(Url)

parsed_data=bs4.BeautifulSoup(respons.text)#fatch data with css selecter

all_link =parsed_data.select('a') #a=anker tag
#print(len(all_link))

for i in all_link:
     # print(i.getText())

   print(i.get('href'))

   print(i.get('title'))

   print(i.attrrs)#fatch all Atribute

