cart = {669856: "milk", 7767854: "bread", 125423: "eggs"}


print(f"{"milk" in cart = }")
print(f"{669856 in cart = }")

print("\n=== Keys ===")
for code in cart.keys():
    print(code)


print("\n=== Items ===")
for code, product_name in cart.items():
    print(f"{code} -> {product_name}")

print("\n=== Values ====")
for product_name in cart.values():
    print(product_name)