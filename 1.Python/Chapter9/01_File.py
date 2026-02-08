'''a= "A very long string with emails."
Ram is volatile .

'''


'''Syntex Of Write File'''


string="I am writing throw file"
with open("file.txt", "a") as f:
    f.write(string)

'''Syntex Of Read File'''

with open("file.txt", "r") as f:
    data = f.read()
    print(data)


'''File has more mode 
a= append {it adds line to the last of a file}
'''

