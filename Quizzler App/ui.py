from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.root = Tk()
        self.root.title("Quizzler")
        self.root.config(bg=THEME_COLOR, padx=50, pady=50)
        self.true = PhotoImage(file="images/true.png")
        self.false = PhotoImage(file="images/false.png")
        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,
            120,
            width=250,
            font=("Arial", 18, "italic"),
            text=""
        )
        self.get_next_question()
        self.score = Label(text=f"score: {self.quiz.score}", bg=THEME_COLOR)
        self.true_button = Button(image=self.true, highlightthickness=0, command=self.true_choice)
        self.false_button = Button(image=self.false, highlightthickness=0, command=self.false_choice)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.score.grid(row=0, column=1)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.root.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have reached the end of the quiz, you got {self.quiz.score}/10 correct."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_choice(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def false_choice(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self, is_true):
        if is_true:
            self.canvas.configure(bg="green")
            self.score.configure(text=f"score: {self.quiz.score}")
        else:
            self.canvas.configure(bg="red")
        self.root.after(1000, self.is_after)

    def is_after(self):
        self.canvas.configure(bg="white")
        self.get_next_question()
