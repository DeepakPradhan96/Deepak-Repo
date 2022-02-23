class Employee:
    increment=1.5 #called class variable

    def __init__(self,fname,lname,salary):           #templete
        self.name=fname
        self.title=lname
        self.salary=salary
        self.increment=1.4 #called instance varible
    def Increment(self):
        # self.salary = self.salary * self.increment  #1st serch on instance  veriable then class verible.
        self.salary=self.salary*Employee.increment


Deepak=Employee('deepak','pradhan',4400)

Rina=Employee('Rina','spradhan',5400)

print(Deepak.salary,Rina.title)
Deepak.Increment()
print(Deepak.salary,Rina.title)

print(Deepak.__dict__) #it Represent all varible present in Instance.

#when we call a method or object self Automatically call