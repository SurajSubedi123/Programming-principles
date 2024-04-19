import turtle
import random

# Set up the screen
#  It normally starts by importing the necessary module called Turtle, which allows us to create graphics. 
#Then, it sets up the game screen, giving it a size of 600x600 pixels with a white background.
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Game")
screen.bgcolor("white")

# Create the player turtle
# A turtle is created to represent the player's character. The turtle is positioned in the middle of the screen. 
#And the turtle player is located with a blue color.

player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)

#Creating the coin
# A yellow circle is created to represent a coin. It is placed at a random position on the screen.
coin = turtle.Turtle()
coin.shape("circle")
coin.color("yellow")
coin.penup()
coin.speed(0)
coin.goto(random.randint(-290, 290), random.randint(-290, 290))

# Create the obstacles
#Five red squares are created to represent obstacles. 
#They are placed at random positions on the screen.
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
#The game listens for keyboard input and calls the corresponding movement functions when arrow keys are pressed.
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop
#The game runs in an infinite loop. if the player turtle has collected the coin, in which case the coin moves to a new position. 
# also checks for collisions between the player turtle and obstacles, resetting the new position to the center. 
# if a collision occurs then the game screen is updated to reflect any changes.
while True:
    # Move the coin if player collects it
    if player.distance(coin) < 20:
        coin.goto(random.randint(-290, 290), random.randint(-290, 290))
    
    # Check for collisions with obstacles
    for obstacle in obstacles:
        if player.distance(obstacle) < 20:
            player.goto(0, 0)  # Reset player position
    
    screen.update()

#refrences: https://www.w3schools.com/python/default.asp
#https://www.python.org/about/gettingstarted
#https://www.geeksforgeeks.org/python-programming-language
