# import the libraries
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time
import random


# Set the starting position for paddles-[left, right]
starting_pos = [(-360.0, 0.0), (360.0, 0.0)]

# Setup Screen:
screen = Screen()
# set the screen background
screen.bgcolor("black")
# set the screen size
screen.setup(width=800, height=600)
# set the window title = ping-pong
screen.title("ping-pong")
# fix animation glitches with tracer
screen.tracer(0)

# Create left and right paddles
left_paddle = Paddle(starting_pos[0])
right_paddle = Paddle(starting_pos[1])

# Initial ball direction changes, x_change, y_change
x_change = random.choice([10, -10])
y_change = random.choice([10, -10])

# Create the ball
ball = Ball(x_change, y_change)

# Generate ScoreBoard
score = Scoreboard()


# bind keys to paddles movement:
screen.onkey(left_paddle.move_up, "q")
screen.onkey(left_paddle.move_down, "a")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.textinput("Start Game", "q - Left handle move up\na -\
 Left handle move down\nUp arrow - Right handle move up\n\
Down arrow - Right handle move down\n\n\
Press Enter to start the game.")

# let keypress register some action
screen.listen()


# Start the game:
game_on = True
while game_on:
    # update screen animation
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.move_speed > 0.3:
        ball.move_speed = 0.3

    # making sure no paddle gets out of view:
    left_paddle.limit_vertical_movement()
    right_paddle.limit_vertical_movement()

    # tackling ball bounce logic
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # when ball collides with any paddles:
    # collision with right paddle:
    if ball.distance(right_paddle) < 60 and ball.xcor() > 330\
            and ball.xcor() < 350:
        ball.bounce_x()
        score.increment_score()
    # collision with left paddle:
    if ball.distance(left_paddle) < 60 and ball.xcor() < -330\
            and ball.xcor() > -360:
        ball.bounce_x()
        score.increment_score()

    # game over if ball touches side walls
    if (ball.xcor() > 395) or (ball.xcor() < -395):
        score.game_over()
        game_on = False

# keep display active till click is registered
screen.exitonclick()
