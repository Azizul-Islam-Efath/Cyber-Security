def Max(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    

num1=int(input("Enter the first number:"))
num2=int(input("Enter the Second number:"))
num3=int(input("Enter the Third number:"))

print("The largest number is : ",Max(num1,num2,num3))
