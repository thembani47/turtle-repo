# a race between two turtles
import random
import time
import turtle

screen = turtle.Screen()
screen.bgcolor('cyan')

# create two players
player_1 = turtle.Turtle()
player_1.color('red')
player_1.shape('turtle')
player_2 = turtle.Turtle()
player_2.color('black')
player_2.shape('turtle')

# move the two turtles
player_1.penup()
player_1.goto(-300, 250)
player_2.penup()
player_2.goto(-300, -250)

# draw the finish line using player two
player_2.forward(600)
player_2.left(90)
player_2.pendown()
player_2.forward(550)
player_2.write("Finish", font=24)

# take player two to the starting position
player_2.penup()
player_2.goto(-300, -250)
player_2.right(90)
player_2.color('orange')

player_1.pendown()
player_2.pendown()

# create a die
die = [1, 2, 3, 4, 5, 6]

# use a for loop to move the turtles forward/race
for i in range(30):
    if player_1.pos() >= (300, 250):
        print('Red Wins the race')
        break
    elif player_2.pos() >= (300, -250):
        print('Orange Wins the race')
        break
    else:
        die_roll1 = random.choice(die)
        player_1.forward(20 * die_roll1)
        time.sleep(1)
        die_roll2 = random.choice(die)
        player_2.forward(20 * die_roll2)
        time.sleep(1)
turtle.done()