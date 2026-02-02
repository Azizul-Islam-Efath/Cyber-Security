'''Create pattern
Example:4

********
*******
******
*****
****
***
**
*
'''


def func(num):
    if(num==0):
        return 0
    else:
        for i in range(num,0,-1):
            print("*"*(i),end=" ")
            print("")
        return "Completed"


num = int(input("Enter number of rows: "))
print("The pattern is :",func(num))
