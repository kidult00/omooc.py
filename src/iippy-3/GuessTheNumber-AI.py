
#import simplegui
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
import math

secret_number = 0
guess_number = 0
num_max = 10
num_min = 0
result = ''
guess_list = []

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
    result = "start"
    num_max = 10
    num_min = 0
    guess_number = 0
    guess_list = []
    
    
    print "secret_number is:",secret_number      #for test


    
def ai_num():
    global num_max,num_min,guess_list
    newAI = (num_max + num_min)/2   # get the new num between secret and guess
    guess_list.append(newAI)
    print "new ai:",newAI   #for test
    print guess_list
    print "You've guessed "+str(len(guess_list))+" times"
    return newAI
    

def compare():
    global secret_number,guess_number,num_max,num_min,result,guess_list
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
         
         #for i in range(len(guess_list)):
          #   guess_list.pop(i)
    
    return result

def draw(canvas):
    global result
    if result == 'low' :
        canvas.draw_text("Nope~ Should be a higher one.",(10,15),12,"black")
    elif result == 'high' :
        canvas.draw_text("Nope~ Should be a lower one." ,(10,15),12,"black")
    elif result == 'bingo':
        canvas.draw_text("\(^o^)/~ Bingo!!" ,(10,15),12,"black")
        canvas.draw_text("Your guess history:"+str(guess_list) ,(10,30),12,"black")
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
