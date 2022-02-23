class Employee:
    def __init__(self,fname,lname,salary):           #templete
        self.name=fname
        self.title=lname
        self.salary=salary

Deepak=Employee('deepak','pradhan',4400)

Rina=Employee('Rina','spradhan',5400)

print(Deepak,Rina.title)