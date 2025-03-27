import json

students = {
        "id":1, "name": "Idan Gangan", "gender": "male", "department": "Accounting", "scnhlool": "Unilorin"
        }

with open("013_data.json", "w") as json_file:
    json.dump(students, json_file)

