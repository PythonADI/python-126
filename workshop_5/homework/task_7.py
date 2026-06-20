def average(numbers: list[int]) -> float:
    total = 0
    for num in numbers:
        total += num
    
    return total / len(numbers)



a = [5, 6, 7, 8, 9]
b = [1, 1, 1, 2, 1, 1, 1, 1]

print(average(a))
print(average(b))



