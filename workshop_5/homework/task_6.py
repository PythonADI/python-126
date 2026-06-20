shopping_list = ['lettuce','egg','tomato','cucumber','oil', 'oil']

word = input("Choose: ").strip().lower()



if word in shopping_list:
    occurence = shopping_list.count(word)
    # inline if
    print(f"Yes - {word} is on the list ({occurence} time{"" if occurence == 1 else "s"})")


    # if occurence > 1:
    #     print(f"Yes - {word} is on the list ({occurence} times)")
    # else:
    #     print(f"Yes - {word} is on the list ({occurence} time)")
else:
    print(f"No - {word} is not on the list")


