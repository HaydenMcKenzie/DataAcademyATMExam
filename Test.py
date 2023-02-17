#Test = (not False) or (not True)
#print(Test)

spam = []

userInput = input("Enter: ")

while userInput != "q":
    if userInput == "1":
        spam.append("Hello")
    elif userInput == "2":
        spam.append("Howdy")
    elif userInput >= "3":
        spam.append("Greatings")

print(spam)