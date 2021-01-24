# http://www.codeskulptor.org/#user45_nnLM70kyJ2_14.py
# Codeskulptor is only compatible with Google Chrome.

# implementation of card game - Memory

import simplegui
import random

# initialize variables
a = list (range(0,8))
b = list (range(0,8))
game_list =a+b

# helper function to initialize globals
def new_game():
    global turn, game_list, exposed, state, click1, click2, card_i
    random.shuffle(game_list)
    exposed = [False for i in range(16)]
    turn = 0 
    state = 0
    click1 = 0 
    click2 = 0
    card_i = 0
    
# define event handlers
def mouseclick(pos):
    global exposed, turn, state, click1, click2, card_i,label
    

    if (exposed[pos[0]//50] == True) and (state != 2):
        label2.set_text("Please select a covered card.")
    else:
        click1 = click2
        click2 = card_i
        card_i = pos[0]//50

        label2.set_text("Enjoy the game!")
        if state == 0:
            state = 1
            if exposed[card_i]== False:
                exposed[card_i]=True
                turn += 1
        elif state == 1:
            state = 2
            if exposed[card_i]== False:
                exposed[card_i]=True
                turn += 1
        else: 
            state = 1
            if game_list[click1] == game_list[click2]:
                exposed[click1] = True
                exposed[click2] = True
            else:
                exposed[click1] = False 
                exposed[click2] = False

            exposed[card_i]=True
            turn += 1
                
    print ""
    print click1,click2
    print exposed
    print game_list
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    i = 0
    for i in range(16):
        if exposed[i] == False:
            canvas.draw_polygon([[50*i, 0],[50*i, 100],[50*i+50, 100],[50*i+50, 0]],1,"Orange","Green")
        elif exposed[i] == True:
            canvas.draw_polygon([[50*i, 0],[50*i, 100],[50*i+50, 100],[50*i+50, 0]],1,"Black","Black")
            canvas.draw_text(str(game_list[i]),[10+50*i, 70],60,"white")
    label.set_text("Turns = " + str(turn//2))
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
label2 = frame.add_label("Enjoy the game!")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubricc
