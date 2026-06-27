"""
Using your own module. Run this file with `python use_my_calc.py` — make sure
my_calc.py sits in the same folder so Python can find it.
"""


if __name__ == "__main__":
    import my_calc
    print(f"{__file__} - {__name__ = }")
    print(my_calc.circle_area(5))         # 78.53975
    print(my_calc.rectangle_area(2, 6))   # 12
    print(f"PI is roughly {my_calc.PI}")

    # you can also pull just the names you need:
    from my_calc import circle_area

    print(circle_area(1))                 # 3.14159
