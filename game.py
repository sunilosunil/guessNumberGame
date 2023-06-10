import random
import turtle
import time
from turtle import *
from tkinter import *

# Generate a random number between 1 and 50 (inclusive)
max_guesses = 6
secret_number = random.randint(1,50)
screen = Screen()

print("Guess a number between 1 and 50")
t = turtle.Turtle() # Create a new turtle object
c = 0
# Loop through guesses until either max_guesses is reached or secret_number is found
for i in range(max_guesses):
    user_input = int(textinput("Number", "Enter the number between 1 and 50"))
    screen.clear()
    c = i+1
    if user_input == secret_number:
        turtle.write(f"Congratulations! \n you guessed the correct number \n after {c} guesses", font=('arial',40,'bold'), align='center')
        turtle.hideturtle()
        #turtle.write()
        break
    elif user_input < secret_number:
        turtle.write(f"Too Low {c} guesses", font=('arial',40,'bold'), align='center')
        turtle.hideturtle()
    else:
        turtle.write(f"Too High {c} guesses", font=('arial',40,'bold'), align='center')
        turtle.hideturtle()
    
    time.sleep(1)
if c == max_guesses:
    screen.clear()
    t.write(f"Game over. \n Only {c} guesses allowed !", font=('arial',40,'bold'), align='center')
    turtle.hideturtle()
turtle.done()