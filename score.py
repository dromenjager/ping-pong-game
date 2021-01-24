from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "bold")


class Scoreboard(Turtle):
    """
    Create Scoreboard for the
    ping-pong game
    """

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto((0.0, 280.0))
        self.write(f"SCORE {self.score}",
                   align=ALIGN,
                   font=FONT
                   )
        self.hideturtle()
        self.speed("fastest")

    def increment_score(self):
        self.score += 1
        self.clear()
        return self.write(f"SCORE {self.score}",
                          align=ALIGN,
                          font=FONT
                          )

    def game_over(self):
        self.goto((0.0, 0.0))
        self.write(f"GAME OVER\nYou Scored {self.score} points",
                   align=ALIGN,
                   font=FONT
                   )
