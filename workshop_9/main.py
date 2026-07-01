import os
import time


pos = (3, 2)
prev_space = 0
m = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 2, 1],
    [1, 1, 1, 1],
]


while True:
    print("\033c")
    
    for row in m:
        for c in row:
            if c == 1:
                print("🌲", end="")
            elif c == 0:
                print("🟩", end="")
            elif c == 2:
                print("🧑‍🌾", end="")
        print()
    
    direction = input(">>> ")

    y, x = pos
    if direction == "d":
        next_pos = (y, x + 1)
    elif direction == "w":
        next_pos = (y - 1, x)
    elif direction == "s":
        next_pos = (y + 1, x)
    elif direction == "a":
        next_pos = (y, x - 1)
    
    if 0 <= next_pos[0] < len(m) and 0 <= next_pos[1] < len(m[y]):
        m[y][x] = prev_space
        y, x = next_pos
        prev_space = m[y][x]
        m[y][x] = 2
        pos = next_pos

