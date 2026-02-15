class Employee:                                 #Creating a class
    Language ="Python"                          #This is a class attribute
    Salary= 1200000
    def __init__(this,name):                    #This is a constructor   syntex  :  def __init__(this,Variable)     this means current obj
        this.name=name                                                            
        
        
    def Display(this):                          #Method
        print("\nPerson Info: ")
        print("Name: ",this.name)
        print("Preffered Language: ",this.Language)
        print("Salary: ",this.Salary)

    

P1=Employee("Raihan")                   #Object
P2=Employee("Rahie")                    #Object
P3=Employee("Efath")                    #Object
P4=Employee("Mishka")                   #Object


P1.Display()                            #Calling method
P2.Display()
P3.Display()
P4.Display()
