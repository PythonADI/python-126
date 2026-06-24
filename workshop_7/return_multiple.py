"""
Returning more than one value from a function.

A function can hand back several values at once by separating them with
commas — Python packs them into a tuple. The caller can unpack them.
"""




def min_and_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return smallest, largest   # this is a tuple: (smallest, largest)


scores = [42, 17, 99, 73, 8]

# unpack the two returned values into two variables
low, high = min_and_max(scores)
print(f"lowest:  {low}")
print(f"highest: {high}")

# or keep them together as one tuple
result = min_and_max(scores)
print(result)
print(f"range is {result[1] - result[0]}")
