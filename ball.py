from turtle import Turtle


class Ball(Turtle):
    """
    Create a ball object
    """

    def __init__(self, inc_x, inc_y):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1.2,
                       stretch_wid=1.2)
        self.color("gold")
        self.penup()
        self.inc_x = inc_x
        self.inc_y = inc_y
        self.move_speed = 0.08

    def move(self):
        """
        move the ball
        """
        new_xcor = self.xcor() + self.inc_x
        new_ycor = self.ycor() + self.inc_y
        self.goto((new_xcor, new_ycor))

    def bounce_y(self):
        """
        Bounce the ball when it
        hits up and bottom walls
        """
        self.inc_y *= -1

    def bounce_x(self):
        """
        Bounce the ball when it hits
        paddles
        """
        self.inc_x *= -1
        self.move_speed *= 0.9
