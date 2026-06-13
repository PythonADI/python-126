shopping = ["milk", "bread", "eggs"]

shopping[0] = "oat milk"      # replace the item at a position
print(shopping)

shopping.append("cheese")     # add one item to the end
print(shopping)

shopping.insert(1, "butter")  # add at a position, push the rest right
print(shopping)

last = shopping.pop()         # remove the last item AND hand it back
print(f"removed: {last}")
print(shopping)

shopping.remove("eggs")       # remove by value
print(shopping)

print(f"{len(shopping)} items left")
