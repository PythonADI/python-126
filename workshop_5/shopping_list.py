shopping_list = []
in_bag = []


while True:
    product = input("Enter product name: ")

    if product.lower() == "done":
        break
    shopping_list.append(product)


for item in shopping_list[:]: 
    is_purchased = input(f"Did you buy {item}? (y / n): ").lower() == "y"
    if is_purchased:
        shopping_list.remove(item)
        in_bag.append(item)

print("\nYou have left:")
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")
