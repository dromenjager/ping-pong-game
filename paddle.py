from turtle import Turtle


class Paddle(Turtle):
    """
    Create the paddle object
    """

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,
                       stretch_len=1),
        self.color("green")
        self.penup()
        self.goto(position)
        self.speed("fast")

    def move_up(self):
        """
        Move the paddle up
        """
        y_corr = self.ycor()
        self.goto(self.xcor(), y_corr+20)

    def move_down(self):
        """
        Move the paddle down
        """
        y_corr = self.ycor()
        self.goto(self.xcor(), y_corr-20)

    def limit_vertical_movement(self):
        """
        Stop the paddle from
        getting out of screen
        """
        if self.ycor() > 270:
            self.goto((self.xcor(), 270))
        elif self.ycor() < -270:
            self.goto((self.xcor(), -270))
