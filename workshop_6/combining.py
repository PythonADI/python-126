students = [
    {"name": "nino", "score": 90},
    {"name": "giorgi", "score": 75},
]

for s in students:
    s["pet"] = "dog"
    print(f'{s["name"]}: {s["score"]}')

for student in students:
    print(student)