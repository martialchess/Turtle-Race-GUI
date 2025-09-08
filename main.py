from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
random.shuffle(colors) # shuffle once so colors are random but unique
y_positions = [-100, -50, 0, 50, 100, 150] # spacing evenly

all_turtles = []

# Create 5 turtles with random colors
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

# Start race only if user placed a bet
race_on = False
if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10) # random step forward
        turtle.forward(rand_distance)

        # Check if turtle crossed the finish line
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"🎉 You won! The {winning_color} turtle is the winner!")
            else:
                print(f"🎉 You lost! The {winning_color} turtle is the winner!")
            break

screen.exitonclick()