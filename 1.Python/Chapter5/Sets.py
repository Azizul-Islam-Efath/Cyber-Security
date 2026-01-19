a=set()# itt is an empty set
b={1,2,3,3,3,4,2,65,33,7,3}
print(b)

'''Set doesnot repeat an integer twice.
it is an unordered list
it cannot be accessed by index no'''

#Method

#.add(Value)
b.add(233)
print(b)

#.remove()
b.remove(1)
print(b)

#pop()
b.pop()     #Removes an element from the set
print(b)

#union(variable)
S1={2,3,1,5,6,4,8}
S2={3,4,2,24,6,7,8,9,0}

print(S1.union(S2))

#intersection-
print(S1.intersection(S2))