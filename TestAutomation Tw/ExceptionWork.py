# any Error We Are Geting on Run Time Is called Run Time Error Or Expeception Error
#try,except,final
try:
     input1=input("enter a no-")
     input2=input('enter 2nd No-')

     c= int(input1)+int(input2)
     print(c)
#Except Execute When try fail
except:
    print('enter a valid no')

finally:
    print('done')