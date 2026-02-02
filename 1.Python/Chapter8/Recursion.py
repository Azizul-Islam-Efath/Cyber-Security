'''Recursion
factorial:5
5*4*3*2*1

factorial:4
4*3*2*1

factorial:n
n*factorial(n-1)

'''

def factorial(num):
    if(num==1 or num==0):
        return 1
    else :
        return num*factorial(num-1)


num=int(input("Enter a number:"))
print(f"Factorial of the number {num} is :",factorial(num))