shopping = ["milk", "bread", "eggs", "cheese"]

# walk the items one by one — just like looping over a string
for item in shopping:
    print(item)

print("---")

# need the position too? loop over the indexes with range(len(...))
for i in range(len(shopping)):
    print(f"{i + 1}. {shopping[i]}")
