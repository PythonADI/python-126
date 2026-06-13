def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


numbers = [70, 85, 90, 60]
avg = average(numbers)
print(avg)

x = [70, 85, 90, 60, 100, 22, 34]
print(average(x))