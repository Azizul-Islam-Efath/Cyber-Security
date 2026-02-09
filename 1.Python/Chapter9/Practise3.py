def generateTable(n):
    table = ""
    for i in range(1,11):
         table +=f"{n} x {i} = {n*i}\n"

    with open(f"MultiPlicationTable/Table_{n}.txt","w") as f :
            f.write(table)

for i in range(21,51):
    generateTable(i)