person = {
    "name": "John", 
    "last_name": "Doe",
    "age": 45,
    "pet": "Dog"
}


print(person)
print(len(person))

print(person["name"])
print(person["last_name"])
# full_name = person["name"] + " " + person["last_name"]
# full_name = f"{person["name"]} {person["last_name"]}"
# evaluation
print(f"{person["name"]} {person["last_name"]}")


deleted_animal = person.pop("pet")
print(person)
print(f"{deleted_animal = }")