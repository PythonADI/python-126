"""
Simple Quiz Game — a trivia quiz that stores questions/answers in a list of dicts, tracks the player's score in a 
dict, and shows results at the end.

  - A questions list where each item is a dict: {"question": "...", "answer": "..."}
  - Loop through each question, ask the player, check if their answer matches
  - Track results in a results dict: {"correct": 0, "wrong": 0}
  - Print a summary at the end
"""

player = {"correct": 0, "wrong": 0}
questions = [
    {
        "question": "What color is the sky?",
        "answers": [
            {"text": "yellow", "is_correct": False},
            {"text": "blue", "is_correct": True}
        ]
    },
    {
        "question": "Capital of Georgia?",
        "answers": [
            {"text": "Tbilisi", "is_correct": True},
            {"text": "Yerevan", "is_correct": False},
            {"text": "Batumi", "is_correct": False},
            {"text": "Kutaisi", "is_correct": False},
        ]
    }
]


for question in questions:
    print(question["question"])
    for i, answer in enumerate(question["answers"]):
        print(f"{i}: {answer["text"]}")
    choice = int(input("Select your answer: "))
    
    chosen_aswer = question["answers"][choice]
    if chosen_aswer["is_correct"]:
        player["correct"] += 1
    else:
        player["wrong"] += 1
    print("=" * 10)

print(player)
