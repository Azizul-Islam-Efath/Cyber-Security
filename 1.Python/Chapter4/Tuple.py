#Tuple is immutable

A = ()
print(type(A))

b=(1,False,"Azizul","Islam",1,1,3.1416)

print(b)

#Methods-
#count(value)  
c=b.count(1)
print(c)

#unpacking tuple-

a,b,c,d,e,f,g=b
print(a,b,c,d,e,f,g)