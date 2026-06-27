"""
my_calc.py — your OWN module.

Any .py file is a module. Put functions and constants you want to reuse in
here, and other files can `import my_calc` to borrow them. Run this file on
its own and the demo at the bottom runs; import it elsewhere and only the
functions and PI come across (the demo stays quiet — see the guard below).
"""
PI = 3.14159



def circle_area(radius):
    return PI * radius * radius


def rectangle_area(width, height):
    return width * height


# This guard means "only run when THIS file is the one being run directly".
# When another file imports my_calc, __name__ is "my_calc", not "__main__",
# so the demo below is skipped.
if __name__ == "__main__":
    print("Quick self-test:")
    print(circle_area(2))        # 12.56636
    print(rectangle_area(3, 4))  # 12
