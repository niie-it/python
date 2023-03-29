import json

with open("Students.json", "r", encoding="utf8") as myfile:
    my_data = json.load(myfile)
    print(my_data)