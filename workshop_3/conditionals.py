weather = input("rainy / windy / sunny: ").lower()

is_rainy = weather == "rainy"
is_windy = weather == "windy"
is_sunny = weather == "sunny"


if is_rainy:
    print("stay at home dry")
elif is_windy:
    print("close the windows")
elif is_sunny:
    print("Let's walk")
else:
    print("This weather condition does not exist in our system")
