# http://www.codeskulptor.org/#user45_3SiLE6hoYv_8.py
# Codeskulptor is only compatible with Google Chrome.

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math

# helper function to start and restart the game
upper_bound =100
trial_number = 1
max_trial = int( math.ceil(math.log(100-0+1)/math.log(2)))
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global trial_number
    
    secret_number = random.randrange(0,upper_bound)
    trial_number = 1
    
    print "New game. Range is [0," + str(upper_bound) + ")."
    print "You can guess " + str(max_trial) + " times."
    print "You may start your first guess."
    print ""
    
    return secret_number 

# define event handlers for control panel
def range100():
    global upper_bound
    global max_trial 
    
    upper_bound = 100
    max_trial = int( math.ceil(math.log(upper_bound-0+1)/math.log(2)))
    new_game()
    
def range1000():
    global upper_bound
    global max_trial 
    
    upper_bound = 1000
    max_trial = int( math.ceil(math.log(upper_bound-0+1)/math.log(2)))
    new_game()
    
def input_guess(guess):
    print "Guess was " + guess
    guess = int (guess)
    
    global trial_number
    
    if guess < secret_number:
        print "Higher"
        print "Number of remaining guesses is " + str(max_trial-trial_number)
        print ""
        
    elif guess > secret_number: 
        print "Lower"
        print "Number of remaining guesses is " + str(max_trial-trial_number)
        print ""

    else:
        print "Correct"
        print "Number of remaining guesses is " + str(max_trial-trial_number)
        print ""
        new_game()
      
    trial_number +=1
     
    if trial_number > max_trial: 
        print "You reached the number of guesses." 
        print "The secret number is " +str(secret_number) + "."
        print ""
        new_game()
    return trial_number
    

# create frame
frame = simplegui.create_frame("Guess the number", 100, 200)

button1 = frame.add_button('Range is [0, 100)', range100)
button2 = frame.add_button('Range is [0, 1000)', range1000)
frame.add_input("What is your guess?", input_guess, 200)

# register event handlers for control elements and start frame

# call new_game 
new_game()
frame.start()
# always remember to check your completed program against the grading rubric
