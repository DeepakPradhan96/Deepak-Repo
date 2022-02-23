# redi+ng Data from File

obj= open('D:\py.txt',"r")

print(obj.read())  ## read All data
# read one line
print(obj.readline())
print(obj.readline(2))
for i in obj.read():
    print(i)

'''x=obj.read()
while(x): #while x exist run loop
    print(x)
    x=obj.read()'''

