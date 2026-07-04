"""
Handman Game 
The concept is to guess a word. 3 attempts.
"""
from random import choice
import time

cities = ["tbilisi","mtskheta", "kazbegi", "telavi", "rustavi", "bolnisi", "dmanisi", "batumi", "poti", "gori", "kutaisi", "kobuleti"]

rand_city = choice(cities)

def hint():
    hint = rand_city.title()[0] + (len(rand_city)- 1)* "_"
    return hint


won = False
attempt = 3

print("Choosing a word...")
time.sleep(2)
print(hint())

while attempt < 3:
    chosen_city = input("What word have I chosen?").lower().strip()

    if chosen_city == rand_city:
        won = True
        break

    print(f"Wrong! Number of attempts:{attempt}")
    attempt += 1



if won:
    print("You won")
else:
    print("You lost")

