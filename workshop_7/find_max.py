import random

# find minimum number
nums = []
for _ in range(10):
    nums.append(random.randint(0, 100))


print(nums)

mn = nums[0]

for num in nums:
    if num < mn:
        mn = num

print(mn)
