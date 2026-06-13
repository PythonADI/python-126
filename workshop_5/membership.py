shopping = ["milk", "bread", "eggs", "milk"]

if "bread" in shopping:
    print("bread is on the list")

if "khinkali" not in shopping:
    print("we forgot the khinkali!")

# how many times does milk appear?
print(shopping.count("milk"))

# `in` works on strings too (same idea as looping over characters)
print("a" in "banana")
print("z" in "banana")
