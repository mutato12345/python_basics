import json
with open("035_signup_data.json", "r") as file:
    
    my_list_dict = json.load(file)

    print("please enter the following details:")

    data_dict = {
            "id": input("ID: "),
            "first_name": input("First Name: "),
            "last_name": input("Last Name: "),
            "email": input("Email: "),
            "password": input("Password: ")
            }
    my_list_dict.append(data_dict)

    with open("035_signup_data.json", "w") as file:
        json.dump(my_list_dict, file, indent=4)
    


