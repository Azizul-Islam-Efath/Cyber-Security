#printing date 

a = input("Write Your Name Here: ")


from datetime import date

today = date.today()
Letter = f'''Dear {a}, You are selected! {today}'''

print(Letter)