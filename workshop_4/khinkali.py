

def prepare_khinkali(has_grass = True):
    print("ვამზადებ ცომს")
    if has_grass:
        print("ვკმაზავ ხორცს")
    print("დავდე ხორცი ცომზე")
    print("მოვახვიე")
    print("მოვხარშე")
    return 1


plate = 0

for i in range(1, 101):
    print(f"preparing {i} khinkali")
    plate += prepare_khinkali()

print(f"there are {plate} khinkali on the plate")