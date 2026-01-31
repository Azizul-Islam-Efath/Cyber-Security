
'''------------------------------While loop-----------------------------'''
print("While Loop Example:")

new =["Azizul","Islam",4,"Efath",False,3.1416,"Sadia Jaman Mishka","Misho"]

i=0

while (i<len(new)):
    print(new[i])
    i=i+1

'''------------------------------For loop-----------------------------'''
print("\nFor Loop Example:")

new_2 =[4,"Efath",False,3.1416,"Sadia Jaman Mishka","Azizul","Islam","Misho"]

for i in new_2:
    print(i)


'''------------------------------For loop with else-----------------------------'''

ex=[1,3,2,4,5,6,4,7,8,9]
print("\nFor Loop with else Example:")

for i in ex:
    print(i)
else:
    print("The loop is ended now.")