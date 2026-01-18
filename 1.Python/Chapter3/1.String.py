
name = "Azizul Islam"

print("My name is ",name)

#string slice
#Positive
nameshort = name[0:6] #including index 0 up to index 5 (index 6 excluded)
#Negative
nameshortneg=name[-5:]

print(nameshort)
print(nameshortneg)

#Concatination
concatedName=nameshort+" "+ nameshortneg
print(concatedName)

#Functions-
#len()
length=len(name) 
print("The length of the String is :",length)

#startswith-     its case sensitive
print("The string name is starting with Azizul? : ",name.startswith("Azizul"))

#endswith()-     its case sensitive
print("The string name is ending with Islam? : ",name.endswith("Islam"))

#lower()-
print("Lower cased name is ",name.lower())

#upper()-
print("Upper cased name is ",name.upper())

#capitalize()-
print("Capitalized String is :",name.capitalize())

#title()-
print("Titled String is :",name.title())

new = "    Azizul Islam Efath     "

#lstrip()-
print("Leading space removed String is :",new.lstrip())

#rstrip()-
print("Trailling space removed String is :",new.rstrip())

#strip()-
print("Stripped String is :",new.strip())

#count(" ")-
print("Frequency of a in the string is",new.count("a"))

#find(" ")-
print("Position of the word Efath in the String is :",new.find("Efath"))    # this finds the word and returns the starting index

#replace(" "," ")-
print("Replaced string is : ",new.replace("Efath"," ").strip())


#Escape sequence -

#.      \n -it creates newline

# \"HI\". it shows the output like.  "HI"


