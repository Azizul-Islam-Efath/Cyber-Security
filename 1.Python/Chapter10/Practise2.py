class Calculator:
    def __init__(self,num):
        self.num=num

    def Square(self):
        square=self.num*self.num
        print(f"Square of the number {self.num} is = {square}")
    def Cube(self):
        Cube=self.num*self.num*self.num
        print(f"Cube of the number {self.num} is = {Cube}")
    def SquareRoot(self):
        SquareRoot=self.num ** 0.5
        print(f"SquareRoot of the number {self.num} is = {SquareRoot}")

    def Calc(self):
        self.Square()
        self.Cube()
        self.SquareRoot()
    
    @staticmethod
    def Greet():
        print("\nHello!. Welcome to the Calculator.")

Num1=Calculator(25)
Num1.Greet()
Num1.Calc()

Num2=Calculator(81)
Num1.Greet()
Num2.Calc()

Num3=Calculator(64)
Num1.Greet()
Num3.Calc()