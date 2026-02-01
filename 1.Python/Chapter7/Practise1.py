print("Printing a Multiplication Table using Nested Loops in Reverse Order:")

num=int(input("Enter a number to print its multiplication table: "))

for i in range(1,11):
    print(f"{num} x {11-i} = {num*(11-i)}")
