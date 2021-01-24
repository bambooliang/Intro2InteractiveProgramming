# http://www.codeskulptor.org/#user45_dq7zWIXxsH_21.py
# Codeskulptor is only compatible with Google Chrome.

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_vel = [0,0]
ball_pos = [300,200]
paddle1_pos = 0
paddle2_pos = 0
paddle1_vel = 0
paddle2_vel = 0
direction = "RIGHT"
fly_up = True
score1 = 0 
score2 = 0
acceleration= 1

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    # Update speed
    ball_vel[0] = random.randrange(1, 4)*acceleration
    ball_vel[1] = random.randrange(1, 3)*acceleration
    
    if direction == "LEFT":
        ball_vel[0] = - ball_vel[0]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,ball_pos  # these are numbers
    global score1, score2  # these are ints
    global acceleration1, acceleration2 
    score1 = 0 
    score2 = 0
    acceleration = 1
    ball_pos = [300,200]
    spawn_ball(direction)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,direction, fly_up
    global acceleration
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball position
    
    if (ball_pos[0] > WIDTH - PAD_WIDTH - BALL_RADIUS) and (direction =="RIGHT"):
        direction ="LEFT"
        if (ball_pos[1] < paddle2_pos or ball_pos[1] > paddle2_pos + PAD_HEIGHT):
            score1 +=1
            ball_pos = [300,200]
            fly_up = True
        else:
            acceleration = acceleration *1.1
            
    if (ball_pos[0] < PAD_WIDTH + BALL_RADIUS) and (direction =="LEFT"):
        direction ="RIGHT"
        if (ball_pos[1] < paddle1_pos or ball_pos[1] > paddle1_pos + PAD_HEIGHT):
            score2 +=1
            ball_pos = [300,200]
            fly_up = True
        else:
            acceleration = acceleration *1.1
            
    spawn_ball(direction)
    
    if (ball_pos[1] <= BALL_RADIUS):
        fly_up = False
    
    if (ball_pos[1] >= HEIGHT - BALL_RADIUS):
        fly_up = True
    
    if fly_up == True:
        ball_vel[1]= - ball_vel[1]
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Yellow", "Green")

    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos+paddle1_vel) >= 0 and (paddle1_pos+paddle1_vel) <= HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel

    if (paddle2_pos+paddle2_vel) >= 0 and (paddle2_pos+paddle2_vel) <= HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos],[PAD_WIDTH, paddle1_pos],[PAD_WIDTH,PAD_HEIGHT+paddle1_pos], [0, paddle1_pos+PAD_HEIGHT]],2, "white") 
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos+PAD_HEIGHT],[WIDTH, PAD_HEIGHT+paddle2_pos],[WIDTH,paddle2_pos]],2, "white")
    
    # draw scores
    canvas.draw_text( "Player 1 (left) score: "+ str(score1) , (20, 20), 20, 'Purple')
    canvas.draw_text( "Player 2 (right) score: " + str(score2), (320, 20), 20, 'Purple')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == 38:
        paddle2_vel -= 5
    elif key == 40:
        paddle2_vel += 5
    elif key == 87:
        paddle1_vel -= 5
    elif key == 83:
        paddle1_vel += 5

    
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Restart', new_game)

# start frame
new_game()
frame.start()
