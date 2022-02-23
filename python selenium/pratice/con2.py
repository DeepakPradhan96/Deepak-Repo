x= int(input('enter a no--'))

if (x%5==0 and x%11==0):
    print(x  ,"is divisible by both 11 and 5 ")
elif x%5==0 :
    print(x , "divisible by 5 only")
elif x%11==0:
    print(x, 'is divible by 11 ')
else:
    print(x,'is  not disible 5 and 11  both')


