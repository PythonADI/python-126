"""
თუ მომხმარებელი 18 წელზე ნაკლებისაა არ შეუშვათ
თუ 27 წლისაა და თან ქვია მარიამი გავუკეთოთ 30% ფასდაკლება
ხოლო თუ ლუწი ასაკისაა და თან გიორგი ქვია, მივცეთ 1 უფასო სასმელი
თუ არადა ჩვეულებრივი მომხმარებელია და შემოვუშვათ
"""
age = int(input("what's your age? "))
name = input("what's your name? ").lower()  

if age < 18:
    print("not allowed")
elif age == 27 and name == "mariami":  
    print("30% discount")
elif age % 2 == 0 or name == "giorgi":  
    print("one free drink")
else:
    print("usual price")