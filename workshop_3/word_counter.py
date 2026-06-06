"""
გვაქვს X სტრინგი
# რამდენი ასო არის სტრინგში
რამდენი სიტყვაა სტრინგში
"""

x = "now this has words"
n = 1
if not x:
    n = 0

for char in x:
    # print(char)
    if char == " ":
        n += 1

print(f"x has {n} words")
print(len(x))
# print(x.count(" ") + 1)
