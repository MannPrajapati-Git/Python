# project : simple quiz application using dictionary

# Step 1: Create the quiz data
quiz = {
    "What is the capital of France?": (["A. Paris", "B. London", "C. Rome", "D. Madrid"], "A"),
    "Which planet is known as the Red Planet?": (["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"], "B"),
    "What is 5 + 3?": (["A. 6", "B. 7", "C. 8", "D. 9"], "C"),
    "Who wrote 'Harry Potter'?": (["A. Shakespeare", "B. J.K. Rowling", "C. Tolkien", "D. Dan Brown"], "B"),
}

score = 0

# Step 3: Ask each question
for question in quiz:
    options, correct_answer = quiz[question]

    print("\n" + question)
    for option in options:
        print(option)

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is", correct_answer)

# Step 4: Final score
print("\nQuiz Over!")
print("You got", score, "out of", len(quiz), "correct.")
