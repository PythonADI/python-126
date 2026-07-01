scores = {
    "natali": 95,
    "mia": 90,
    "emily": 60
}

choose_name = input("Whose score? ").lower().strip()
def chosen():
    if choose_name in scores:
        return scores[choose_name]
    
try:
    print(f"{choose_name}'s score is {chosen()}")
except KeyError:
    print(f"No score recorded for {choose_name}")
finally:
    print("Well done!")