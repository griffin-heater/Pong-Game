from turtle import Turtle, Screen
from paddle import Paddle, L_PADDLE, R_PADDLE
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen() # Defines the screen for the game
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0) # Stops annimation of game

r_paddle = Paddle(position=R_PADDLE)
l_paddle = Paddle(position=L_PADDLE)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
# Right paddle controls: 
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
# Left paddle controls:
screen.onkey(l_paddle.go_up, 'w') # One bug to note: turtle limits onkey press for w and s
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collison with wall and bounces off wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.wall_bounce()
        
    # Detect collision with paddles and bounces off paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # Detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    # Detect when L paddle misses    
    if ball.xcor() < -385:
        ball.reset_position()
        scoreboard.r_point()
        
screen.exitonclick()