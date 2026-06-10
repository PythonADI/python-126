def sum_to_n(n):
    total = 0
    for num in range(n + 1):
        total += num
    return total


x = sum_to_n(10)
print(x)
