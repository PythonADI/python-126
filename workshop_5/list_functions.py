# a function can take a whole list and hand back one answer


def total(numbers):
    result = 0
    for n in numbers:
        result += n
    return result


def average(numbers):
    return total(numbers) / len(numbers)


scores = [70, 85, 90, 60]

print(f"total:   {total(scores)}")
print(f"average: {average(scores)}")

# the function works on any list you pass it
print(total([1, 2, 3]))
