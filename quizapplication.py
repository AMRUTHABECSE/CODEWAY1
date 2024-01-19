import random

class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A. Paris", "B. London", "C. Berlin", "D. Rome"],
                "correct_answer": "A"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A. Mars", "B. Jupiter", "C. Venus", "D. Saturn"],
                "correct_answer": "A"
            },
            # Add more questions as needed
        ]
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("You will be asked multiple-choice questions. Choose the correct option.")

    def display_question(self, question_data):
        print("\n" + question_data["question"])
        for option in question_data["options"]:
            print(option)

    def get_user_answer(self):
        return input("Enter your answer (A/B/C/D): ").upper()

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.")

    def display_final_results(self):
        print(f"\nYour final score: {self.score}/{len(self.questions)}")

    def play_quiz_game(self):
        self.display_welcome_message()

        random.shuffle(self.questions)

        for question_data in self.questions:
            self.display_question(question_data)
            user_answer = self.get_user_answer()
            self.evaluate_answer(user_answer, question_data["correct_answer"])

        self.display_final_results()

if __name__ == "__main__":
    while True:
        quiz = QuizGame()
        quiz.play_quiz_game()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing. Goodbye!")
            break
