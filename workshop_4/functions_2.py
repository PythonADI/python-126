

UPPER_THRESHOLD = 20
LOWER_THRESHOLD = 16

def control_temperature(temp, lower_threshold = 10, upper_threshold = 20):
    if temp > upper_threshold:
        print("Turn on AC")
    elif temp < lower_threshold:
        print("Turn on Heating")


# def control_temperature(temp):
#     if temp > UPPER_THRESHOLD:
#         print("Turn on AC")
#     elif temp < LOWER_THRESHOLD:
#         print("Turn on Heating")

while True:
    temp = float(input(">>> "))
    control_temperature(temp)

