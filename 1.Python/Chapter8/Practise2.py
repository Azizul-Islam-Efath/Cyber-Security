'''Calcius to farhenheit conversion'''

def Converter(C):
    F = (C * 9/5) + 32

    print(f"The ferhenheit Scale of the Temp {C} Calcius is {F}")


Temp=int(input("Put the Temperature here:"))
Converter(Temp)
