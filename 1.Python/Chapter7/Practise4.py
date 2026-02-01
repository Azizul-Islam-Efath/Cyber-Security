'''Create pattern
Example:4
*
***
*****
*******
********

'''

num = int(input("Enter number of rows: "))

for i in range(num+1):

    print("*"*(i),end=" ")
    print("")

