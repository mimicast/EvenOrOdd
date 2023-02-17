selNumber = int(input("Give me a number. I'll guess if it's Odd or Even."))

modResult = selNumber % 2

if modResult == 0:
    print("The number is Even.")
else:
    print("The Number is Odd.")