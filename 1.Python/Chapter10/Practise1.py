class Programmer:
    company="Microsoft"
    def __init__(self,name,age,id,salary):
        self.name=name
        self.age=age
        self.id=id
        self.salary=salary
    
    def display(self):
        print(f"\nCompany name: {self.company}\nEmployee ID: {self.id}\nEmployee Name: {self.name}\nEmployee Age: {self.age}\nEmployee Salary: {self.salary}")

Emp1=Programmer("Azizul Islam",23,"OIC1298",30000)
Emp2=Programmer("Aminul Islam",28,"OIC1568",50000)
Emp3=Programmer("Resadul Islam",33,"OIC1268",120000)
Emp4=Programmer("Tanjil Islam",33,"OIC1496",30000)
Emp5=Programmer("Refayat Islam",20,"OIC1345",20000)



Emp1.display()
Emp2.display()
Emp3.display()
Emp4.display()
Emp5.display()
