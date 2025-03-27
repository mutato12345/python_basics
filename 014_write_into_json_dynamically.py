import json
user = {
        "id": input("Enter ID: "),
        "first_name": input("Enter First Name: "),
        "last_name": input("Enter Last Name: "),
        "email":input("Enter email: "),
        "password":input("Enter password:")
        }

with open("015_register.json", "w")as json_file:
    json.dump(user, json_file)
