#Creating a List

new =["Azizul","Islam",4,"Efath",False,3.1416]
new[4]=True

print(new)
print("\n")
#Methods in List

# sort()-
#print("The sorted list is:",new.sort())

# reverse()-
new.reverse()
print("The Reversed list is:",new)
print("\n")

# append(" ")-
new.append("Sadia Jaman Mishka")
print("Append Sadia jaman Mishka at the end of the List :",new)
print("\n")

#insert(index," ")-
new.insert(2,"Misho")
print("Insert at a Index of the list :",new)
print("\n")

#pop(index)-
new.pop(4)
print("Pop index 4: ",new)
print("\n")

#remove(value)-
new.remove(3.1416)
print("Remove the value of 3.1416",new)
print("\n")

new.reverse()
print("The final string is :",new)