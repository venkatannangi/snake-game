from turtle import Turtle

SCORE_BOARD_POSITION = (0, 270)
SCORE_BOARD_FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(SCORE_BOARD_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", font=SCORE_BOARD_FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", font=SCORE_BOARD_FONT, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
