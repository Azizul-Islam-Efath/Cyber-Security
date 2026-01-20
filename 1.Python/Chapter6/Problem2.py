comment=input("Enter a comment: ")

if("Make a lots of money" in comment or
   "buy now" in comment or
   "subscribe this" in comment or
   "click this" in comment):
    print("This is a spam.")

else:
    print("This is not a spam.")