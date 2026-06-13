nums = [10, 20, 30, 40, 50]

print(nums[1:4])   # from 1 up to (but not including) 4  ->  [20, 30, 40]
print(nums[:3])    # the first three
print(nums[2:])    # from 2 to the end
print(nums[:])     # the whole list (a copy)

# a slice is itself a list
first_two = nums[:2]
print(first_two)

# slicing works on strings too
word = "programming"
print(word[0:4])   # the first 4 letters (0, 1, 2, 3) -> "prog"
