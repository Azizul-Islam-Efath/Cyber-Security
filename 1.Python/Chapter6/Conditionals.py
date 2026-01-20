#If-elif-else

Age = int(input("Enter your age: "))

if Age < 0:
    print("Age cannot be negative!")
elif Age < 18:
    print("You are not an Adult")
else:
    print("You are an Adult")
