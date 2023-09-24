from turtle import Screen
from src.paddle import Paddle
from src.ball import Ball
from src.scoreboard import Scoreboard
from time import sleep


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.clear()
        scoreboard.goto(-100, 200)
        scoreboard.write(scoreboard.l_score, align='center',
                         font=('Courier', 80, 'normal'))
        scoreboard.goto(100, 200)
        scoreboard.write(scoreboard.r_score, align='center',
                         font=('Courier', 80, 'normal'))

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.clear()
        scoreboard.goto(-100, 200)
        scoreboard.write(scoreboard.l_score, align='center',
                         font=('Courier', 80, 'normal'))
        scoreboard.goto(100, 200)
        scoreboard.write(scoreboard.r_score, align='center',
                         font=('Courier', 80, 'normal'))

screen.exitonclick()
