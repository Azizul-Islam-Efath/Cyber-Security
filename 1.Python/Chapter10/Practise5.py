from random import randint

class Train:
    def __init__(self,TrainNo):
        self.TrainNo=TrainNo
        
    def Book(self,fm,to):
        print(f"\nTicket is booked in train no : {self.TrainNo} \nFrom : {fm}\nTo: {to}")

    def getStatus(self):
        print(f"\nTrain no : {self.TrainNo} is at Location : {randint(100,150)}.{randint(150,200)}.{randint(140,160)}.{randint(120,140)}")

    def getFare(self,fm,to):
        print(f"\nTicket fare in train no : {self.TrainNo} is : {randint(200,1252)}TK\nFrom : {fm}\nTo : {to}")


T=Train(randint(1545,1898))
T.Book("Dhaka","Chittagong")
T.getStatus()
T.getFare("Dhaka","Chittagong")
