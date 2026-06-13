# start with an empty list, then grow it one item at a time
squares = []

for n in range(1, 6):
    squares.append(n * n)

print(squares)                      # [1, 4, 9, 16, 25]
print(f"built {len(squares)} squares")

# the same pattern: keep only the even numbers from 1..10
evens = []
for n in range(1, 11):
    if n % 2 == 0:
        evens.append(n)

print(evens)                        # [2, 4, 6, 8, 10]
