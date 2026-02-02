'''Sum of n natural numbers using recursive function'''

def Sum(n):
    if n < 0:
        print("You have inserted a negative integer.")
        return 0
    elif n == 0:
        return 0
    else:
        return n + Sum(n - 1)

num = int(input("Enter a number: "))
print(f"The sum of the natural numbers from 0 to {num} is: {Sum(num)}")
