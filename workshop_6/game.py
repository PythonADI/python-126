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


def ask(question):
    print(question["question"])


def render_answers(answers):
    for i, answer in enumerate(answers):
        print(f"{i}: {answer["text"]}")

def get_user_answer(question):
    render_answers(question["answers"])
    return question["answers"][int(input("Select your answer: "))]

def is_answer_correct(answer):
    return answer["is_correct"]


def game_loop():
    for question in questions:
        ask(question)
        chosen_aswer = get_user_answer(question["answers"])

        if is_answer_correct(chosen_aswer):
            player["correct"] += 1
        else:
            player["wrong"] += 1
        print("=" * 10)


game_loop()
print(player)
