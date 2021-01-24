# http://www.codeskulptor.org/#user45_RvzcFPWOpD_2.py
# Codeskulptor is only compatible with Google Chrome.

# template for "Stopwatch: The Game"

# import modules
import simplegui
import math

# define global variables
position_time = [120, 150]
position_count = [250, 20]
width = 300
height = 300
interval = 100
second_count = 0
reset_time = False 
s_trial = 0
t_trial = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(second_count):      
    A = 0
    B = 0
    C = 0
    D = 0
    A = int(math.floor(second_count/600))
    B = int(math.floor((second_count - A*600)/100))
    C = int(math.floor((second_count - A*600-B*100)/10))
    D = int(second_count - A*600-B*100 - C*10)
    formatted_time = str(A)+":"+str(B)+str(C)+"."+str(D)
    return formatted_time

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer
    global reset_time
    reset_time = False
    timer.start()

def stop():
    global timer
    global reset_time
    global s_trial
    global t_trial

    reset_time = False 
    timer.stop()
    
    A = int(math.floor(second_count/600))
    B = int(math.floor((second_count - A*600)/100))
    C = int(math.floor((second_count - A*600-B*100)/10))
    D = int(second_count - A*600-B*100 - C*10)
    
    if D == 0:
        s_trial +=1
    t_trial +=1
    
def reset():
    global timer
    global second_count
    global s_trial
    global t_trial
    global reset_time
    
    second_count = 0
    s_trial = 0
    t_trial = 0
    reset_time = True
    timer.stop()

# define event handler for timer with 0.1 sec interval
def increment():
    global second_count 
    if reset_time == True:
        second_count = 0
        return second_count
    second_count +=1 
    return second_count

# define draw handler
def draw(canvas):
    show_time = format(second_count)
    succesful_trial = str(s_trial)
    total_trial = str(t_trial)
    show_count = succesful_trial + "/" + total_trial
    canvas.draw_text(show_time, position_time, 36, "White")
    canvas.draw_text(show_count, position_count, 20, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", width, height)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, increment)

# start frame
frame.start()
start_button = frame.add_button('Start', start)
stop_button = frame.add_button('Stop', stop)
reset_button = frame.add_button('Reset', reset)

# Please remember to review the grading rubric
