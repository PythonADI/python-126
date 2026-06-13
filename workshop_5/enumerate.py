shopping_list = ["Onion", "Oil", "Eggs", "Ketchup", "Bread", "Milk"]

# for i in range(len(shopping_list)):
#     print(f"{i + 1}. {shopping_list[i]}")

# for i, item in enumerate(shopping_list, 1):
#     print(f"{i}. {item}")


print("\n=== Last 3 ===")
for item in shopping_list[-3:]:
    print(item)

print("\n=== First 3 ===")
for item in shopping_list[:3]:
    print(item)

print("\n=== Every 2 ===")
for item in shopping_list[1::2]:
    print(item)

print("\n=== Reverse ===")
for item in shopping_list[::-1]:
    print(item)