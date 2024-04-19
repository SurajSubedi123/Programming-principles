import turtle
import random

# Set up the screen

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Game")
screen.bgcolor("white")

# Create the player turtle

player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)

#Creating the coin

coin = turtle.Turtle()
coin.shape("circle")
coin.color("yellow")
coin.penup()
coin.speed(0)
coin.goto(random.randint(-290, 290), random.randint(-290, 290))

# Create the obstacles

obstacles = []
for _ in range(5):
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("red")
    obstacle.penup()
    obstacle.speed(0)
    obstacle.goto(random.randint(-290, 290), random.randint(-290, 290))
    obstacles.append(obstacle)

# Function to move the player
def move_up():
    y = player.ycor()
    player.sety(y + 20)

def move_down():
    y = player.ycor()
    player.sety(y - 20)

def move_left():
    x = player.xcor()
    player.setx(x - 20)

def move_right():
    x = player.xcor()
    player.setx(x + 20)

# Keyboard bindings

screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop

while True:
    # Move the coin if player collects it
    if player.distance(coin) < 20:
        coin.goto(random.randint(-290, 290), random.randint(-290, 290))
    
    # Check for collisions with obstacles
    for obstacle in obstacles:
        if player.distance(obstacle) < 20:
            player.goto(0, 0)  # Reset player position
    
    screen.update()
