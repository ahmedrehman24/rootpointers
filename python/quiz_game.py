questions = {
    "Capital of Germany? ": "berlin",
    "5 + 5? ": "10"
}

score = 0

for question, answer in questions.items():
    user = input(question).lower()
    if user == answer:
        score += 1

print("Score:", score)
