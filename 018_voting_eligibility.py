age = int(input("Enter ypour age: "))
nationality = input("Enter your nationality: ")

if age >= 18 and nationality == "Nigerian":
    print("You are elibible to vote in Nigeria.")
    
elif age < 18 and nationality == "Nigerian":
    print("You are too young to vote.")
else:
    print("You mus be a Nigerian citizen to vote here.")

