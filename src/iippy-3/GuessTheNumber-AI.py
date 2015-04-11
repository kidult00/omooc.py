# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

#import simplegui
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
import math

num_max = 10
num_min = 0
secret_number = 0
guess_number = 0
result = ''

# helper function to start and restart the game
# def new_game():
#     # initialize global variables used in your code here
#     global secret_number,result
#     secret_number = random.randrange(0, 10)
#     result = 'start'
# #for test	
#     print secret_number 


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number,num_max,num_min
    secret_number = random.randrange(0, 10)
    print "New game? Welcome~"
    print ""
    num_max = 10
    num_min = 0
    guess_number = 0
    
#for test
    print "secret_number is:",secret_number 


    
def ai_num():
    global num_max,num_min
    newAI = (num_max + num_min)/2

    print "new ai:",newAI
    return newAI
    

def compare():
    global secret_number,guess_number,num_max,num_min,result
    guess_number = ai_num()
    print "Your guess was: ",guess_number
    if secret_number > guess_number :
         result = 'low'
         num_min = guess_number     # set the new min
    elif secret_number < guess_number :
         result = 'high'
         num_max = guess_number     # set the new max
    else:
         result = 'bingo'
    
    return result

def draw(canvas):
    global result
    if result == 'low' :
        canvas.draw_text("Nope~ Should be a higher one.",(10,15),12,"black")
    elif result == 'high' :
        canvas.draw_text("Nope~ Should be a lower one." ,(10,15),12,"black")
    elif result == 'bingo':
        canvas.draw_text("\(^o^)/~ Bingo!!" ,(10,15),12,"black")
    else:
        canvas.draw_text("Welcome~" ,(10,15),12,"black")
    
# create frame
frame = simplegui.create_frame('Guess the number', 300, 300)
frame.set_canvas_background("White")
frame.set_draw_handler(draw)

# create UI elements
frame.add_label('Welcome to the game!')
frame.add_label('')
frame.add_button('Take a [0,100) guess',range100,200)
frame.add_label('')
frame.add_button('start',compare,200)
#frame.add_input('Take a guess (integer only please)', compare, 200)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
#new_game()


# always remember to check your completed program against the grading rubric
