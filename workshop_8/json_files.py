import json


data = json.load(open("/Users/sds-ge573/PycharmProjects/python-126/workshop_8/products.json"))

print(type(data))
print(data)
print(data["products"][0]["title"])
