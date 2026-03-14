'''
Create a class pets from a class Animals nd further create a class dog from pets .
Add a method barks to class dog  
'''

class Animals:
    def show1(self):
        print("This is animal class.")


class pet(Animals):
    def show2(self):
        print("This is a pet.")

class Dog(pet):
    def show3(self):
        print("This is Dog.")

    def bark(self):
        print("                                 Dog barks..Also you👻\n") 


A= Dog()

A.show1()
A.show2()
A.show3()
A.bark()