'''Create star pattern
Example:4
   *
  ***
 *****
*******

'''

num = int(input("Enter number of rows: "))

for i in range(num+1):
    print(" "*(num-i),end=" ")
    print("*"*(2*i-1),end=" ")
    print("")

