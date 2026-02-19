class Company:
    Cname="SR IT FIRM."
    def Show(self):
        print(f"\nThe name of the Company is {self.Cname}")

class Employee(Company):
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def Display(self):
        print(f"Employee name : {self.name}.\nEmployee Salary : {self.salary}")


Person1=Employee("Azizul Islam",300000)
Person1.Show()
Person1.Display()

Person2=Employee("Sadia Jaman",200000)
Person2.Show()
Person2.Display()

Person3=Employee("Efath",330000)
Person3.Show()
Person3.Display()

Person4=Employee("Mishka",600000)
Person4.Show()
Person4.Display()

