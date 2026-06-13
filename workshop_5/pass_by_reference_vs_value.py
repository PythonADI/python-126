def f():
    print(f"{a = }")
    return a + 1


a = 5

print(a)
a = f()
print(a)