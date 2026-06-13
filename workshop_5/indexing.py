shopping = ["milk", "bread", "eggs", "cheese"]

print(shopping[0])   # the first item — counting starts at 0
print(shopping[1])
print(shopping[-1])  # the last item
print(shopping[-2])  # second from the end

print(len(shopping))                 # 4 items
print(shopping[len(shopping) - 1])   # the last item, the long way

# shopping[4]  ->  IndexError: list index out of range
# there is no item at position 4 — the last one is at 3
