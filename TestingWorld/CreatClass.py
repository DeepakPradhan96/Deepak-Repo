#function Inside Class with Argument
class A :
    def sum (self,a,b):
        c=a+b
        print(c)

    def Multiply(self,a,b):
        c=a*b
        return c
'''obj=A()
obj.sum(1,2)
x=obj.Multiply(10,2)
print(x)'''

#Constructor = __init()__ & 1st Argument Is Always Self is called Automaticaly When Object created & it Take Arugument Also
# #Constructer never Return Any Value,it Use For Intialization.

class B(A):
    def __init__(self,a,b):
        print('It is A Constructer')
        c=a+b
        #return c
        print(c)

obj1=B(10,20)

x=obj1.Multiply(20,3)
print(x)