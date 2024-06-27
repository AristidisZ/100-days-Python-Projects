from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Labels
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="",
                                                     fill="black",
                                                     font=("Arial", 20, "italic"),
                                                     width=280)

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.my_no = PhotoImage(file="./images/false.png")
        self.button_no = Button(image=self.my_no, highlightthickness=0, bg=THEME_COLOR, command=self.negative)
        self.button_no.grid(column=1, row=2)

        self.my_yes = PhotoImage(file="./images/true.png")
        self.button_yes = Button(image=self.my_yes, bg=THEME_COLOR, highlightthickness=0, command=self.positive)
        self.button_yes.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="This is the end")
            self.button_no.config(state="disabled")
            self.button_yes.config(state="disabled")

    def negative(self):
        answer = "False"
        is_wrong = self.quiz.check_answer(answer)
        self.feedback(is_wrong)

    def positive(self):
        answer = "True"
        is_right = self.quiz.check_answer(answer)
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

# ui = QuizInterface()
