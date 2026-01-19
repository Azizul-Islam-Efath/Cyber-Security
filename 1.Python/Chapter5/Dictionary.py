Grade ={
    "Efath":"A",
    "Mishka":"A+",
    "Joyonto":"A-",
    "Maria":"A"
}

print(Grade,type(Grade ))

#methods

#.items()
print(Grade.items())    #It shows the items in pair with corresponding to the key:value

#.keys()
print(Grade.keys())     #It prints the key value of the dic.

#.values()
print(Grade.values())      #It prints the values of the dictionary

#update()
Grade.update({"Efath":"A+"})
print(Grade )

#get()
print(Grade.get("Efath"))

#pop("Key" )-
Grade.pop("Joyonto")
print(Grade)