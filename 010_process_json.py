import json

with open("009_data.json", "r") as file:
    
    car = json.load(file)

print(car["brand"])

print(car.get("year"))

print(car["features"])

print(car["engine"]["horsepower"])

car["year"] = 2025

car["speed"] = "180km/h"

car.update({"country": "japan"})

del car["color"]

car.pop("model")

with open("011_new_data.json", "w") as file:
    json.dump(car, file)

    print(len(car))

    print(car.keys())
    print(car.values())
    print(car.items())

    for key in car:
        print(key)

        for key, value in car.items():
            print(f"{key}: {value}")



