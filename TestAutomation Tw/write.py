obj= open('D:\py.txt',"w")
obj1= open('D:\py.txt',"a")
obj.write('hello this is new data')
obj1.write('\n add data')

print(obj.tell())
obj.close()
