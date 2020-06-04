from random import choice

questions = ["Will I go to Hell?: ", "Am I gay?: ", "Am I a loser?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why? ").strip().lower()

print("Oh... Okay")
