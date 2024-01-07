import tkinter as tk
import random

class Question:
    def __init__(self, question_text, options, correct_option):
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option

def main():
    questions = [
        Question("What is your college name?", ["TKR", "MVSR", "SPHN", "VBIT"], "SPHN"),
        Question("Which course are you studying?", ["AIML", "CS", "DS", "IOT"], "AIML"),
        Question("What is the capital of India?", ["New Delhi", "Telangana", "Tamil Nadu", "Mumbai"], "New Delhi"),
    ]

    root = tk.Tk()
    root.configure(bg="black")
    app = QuizApp(root, questions)

    root.mainloop()

class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.current_question_index = 0
        self.correct_answers = 0
        self.wrong_answers = 0

        self.master.title("Quiz App")
        self.master.geometry("500x300")
        self.master.configure(bg="black")

        self.question_label = tk.Label(master, text="", font=("Helvetica", 12), fg="white", bg="black")
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(master, text="", command=lambda i=i: self.answer_question(i), width=20, height=2, fg="white", bg="black")
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.result_label = tk.Label(master, text="", font=("Helvetica", 12), bg="black")
        self.result_label.pack(pady=5)

        self.next_question()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.display_question(question)
            self.current_question_index += 1
        else:
            self.show_results()

    def display_question(self, question):
        self.reset_colors()
        self.question_label.config(text=question.question_text)
        options = question.options.copy()
        random.shuffle(options)
        for button, option in zip(self.option_buttons, options):
            button.config(text=option)

    def answer_question(self, selected_option_index):
        question = self.questions[self.current_question_index - 1]
        selected_option = self.option_buttons[selected_option_index].cget("text")

        if question.correct_option == selected_option:
            self.correct_answers += 1
            self.option_buttons[selected_option_index].config(bg="green")
        else:
            self.wrong_answers += 1
            self.option_buttons[selected_option_index].config(bg="red")

        self.master.after(1000, self.next_question)  # Delay before moving to the next question

    def show_results(self):
        self.result_label.config(text=f"Correct: {self.correct_answers}  |  Wrong: {self.wrong_answers}", fg="white")

    def reset_colors(self):
        self.result_label.config(text="")
        for button in self.option_buttons:
            button.config(bg="black")

if __name__ == "__main__":
    main()
