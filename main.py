# main.py
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick
import time

# Setup the game screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Brick Breaker")
screen.tracer(0)  # Turns off animation for smoother updates

# Create game elements
paddle = Paddle((0, -250))  # Create paddle at the bottom center
ball = Ball()                # Create the ball
scoreboard = Scoreboard()    # Create the scoreboard

# Create a list to hold bricks
bricks = []
for y in range(195, 100, -30):  # Create rows of bricks
    for x in range(-350, 380, 70):  # Create bricks in each row
        brick = Brick((x, y))
        bricks.append(brick)  # Add brick to the list

# Event listeners for paddle movement
screen.listen()
screen.onkey(paddle.go_left, "Left")   # Move paddle left
screen.onkey(paddle.go_right, "Right")  # Move paddle left
screen.onkey(paddle.go_left, "a")
screen.onkey(paddle.go_right, "d")
# Move paddle right

game_is_on = True  # Flag to control the game loop
while game_is_on:
    time.sleep(ball.move_speed)  # Control the speed of the game
    screen.update()              # Update the screen
    ball.move()                  # Move the ball

    # Wall collision detection
    if ball.ycor() > 280:  # Bounce off the top wall
        ball.bounce_y()
    if ball.xcor() > 350 or ball.xcor() < -350:  # Bounce off side walls
        ball.bounce_x()

    # Paddle collision detection
    if ball.distance(paddle) < 50 and ball.ycor() == -240:  # Check for paddle collision
        ball.bounce_y()

    # Brick collision detection
    for brick in bricks:
        if ball.distance(brick) < 30:  # Check for collision with bricks
            ball.bounce_y()            # Bounce the ball
            brick.destroy()             # Remove the brick from the screen
            bricks.remove(brick)        # Remove brick from the list
            scoreboard.add_score()       # Update the score

    # Ball misses the paddle
    if ball.ycor() < -300:  # Check if ball is below the paddle
        game_is_on = False  # End the game
        scoreboard.goto(0, 0)  # Move scoreboard to center
        scoreboard.write("Game Over", align="center", font=("Courier", 50, "bold"))

screen.exitonclick()  # Wait for a click to exit
