items = []
item_count = int(input("How many items? "))

for _ in range(item_count):
    item = input("Item: ")
    items.append(item)


print(items)
print(f"You aded {len(items)} items")