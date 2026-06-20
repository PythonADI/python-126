grades = {"ნინო": 90, "გიორგი": 75, "მარიამი": 88}
total = 0
for name, grade in grades.items():
    print(f"{name}: {grade} ქულა")
    total += grade

print(f"ჯამში {len(grades)} მოსწავლე")
print(f"საშუალო ქულა: {total / len(grades)}")