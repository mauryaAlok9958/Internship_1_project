class Quiz:
    def __init__(self, questions, options, answers):
        self.questions = questions
        self.options = options
        self.answers = answers
        self.guesses = []
        self.score = 0
        self.question_num = 0

    def start_quiz(self):
        for question in self.questions:
            print("----------------------")
            print(question)
            for option in self.options[self.question_num]:
                print(option)

            guess = input("Enter (A, B, C, D): ").upper()
            self.guesses.append(guess)
            self.evaluate_answer(guess)
            self.question_num += 1

        self.show_results()

    def evaluate_answer(self, guess):
        if guess == self.answers[self.question_num]:
            self.score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{self.answers[self.question_num]} is the correct answer")

    def show_results(self):
        print("----------------------")
        print("       RESULTS        ")
        print("----------------------")

        print("answers: ", end="")
        for answer in self.answers:
            print(answer, end=" ")
        print()

        print("guesses: ", end="")
        for guess in self.guesses:
            print(guess, end=" ")
        print()

        self.score = int(self.score / len(self.questions) * 100)
        print(f"Your score is: {self.score}%")


def main():
    questions = (
        "How many elements are in the periodic table?: ",
        "Which animal lays the largest eggs?:",
        "What is the most abundant gas in Earth's atmosphere?: ",
        "How many bones are in the human body?: ",
        "Which planet in the solar system is the hottest?: "
    )

    options = (
        ("A. 116", "B. 117", "C. 118", "D. 119"),
        ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
        ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
        ("A. 206", "B. 207", "C. 208", "D. 209"),
        ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
    )

    answers = ("C", "D", "A", "A", "B")

    quiz = Quiz(questions, options, answers)
    quiz.start_quiz()


if __name__ == "__main__":
    main()
