nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nums.append(11)
print(nums)

nums.pop()
print(nums)
nums.insert(0, -1)
print(nums)
nums[0] = 0
print(nums)
print(len(nums))
nums.append(11)
nums.insert(len(nums) // 2, 25)
print(nums)
