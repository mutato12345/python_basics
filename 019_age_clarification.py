age = int(input("Enter Age: "))
if age < 13:
    print("You are a child.")
    
elif 13 <= age <= 19:
    print("You are a teenager.")

elif 20 <= age <= 59:
    print("You are an adult.")

elif age >= 60:
    print("You are a senior citizen.")
