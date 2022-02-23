#nested disc
odisc={'k1':{'id':1,'pass':321},
       'k2':{'id':2,'pass':358},
       'k3':{'id':3,'pass':851}}

print(odisc['k1']['pass'])
print(odisc['k3']['id'])

#adding value to disc

odisc["k4"]={'id':4,'pass':456}
print(odisc)
print(odisc['k4']['id'])

#add value to internal disc

odisc['k4']['id']=5
odisc['k4']['pass']=['test']
print(odisc)





