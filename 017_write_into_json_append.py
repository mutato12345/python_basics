import json
with open("016_data.json", "r") as file:
          my_list_dict = json.load(file)

          data_dict = {
          "id": input("Enter ID: "),
          "first_name": input("Enter First Name: "),
          "last_name": input("Enter last Name: "),
          "email": input("Enter Email: "),
          "password": input("Enter Password: ")
          }

          my_list_dict.append(data_dict)
          

          with open("016_data.json", "w") as file :

              json.dump(my_list_dict, file)


