#-*- coding: utf-8 -*-

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
done_list = []
guess_time = 0
interval = 500
step = 0    # for replay
y_pos = 10

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
    global secret_number,num_max,num_min,guess_number,result,guess_list,guess_time,y_pos
    secret_number = random.randrange(0, 10)
    print "New game? Welcome~"
    result = "start"
    num_max = 10
    num_min = 0
    guess_number = 0
    guess_list = []
    done_list = []
    guess_time = 0
    y_pos = 10
    
    print "secret_number is:",secret_number      #for test


# generate the right number according to the clue    
def ai_num():
    global num_max,num_min,guess_list,newAI
    newAI = (num_max + num_min)/2   # get the new num between secret and guess
    
    print "new ai:",newAI   #for test
    print guess_list
    print "You've guessed "+str(len(guess_list))+" times"
    return newAI
    
# compare the secret num & the ai num
def compare():
    global secret_number,guess_number,num_max,num_min,result,guess_list,done_list,guess_time,y_pos
    guess_time += 1
    guess_number = ai_num()
    y_pos += 15
    
    print "Your guess was: ",guess_number
    
    if secret_number > guess_number :
         result = 'low'
         num_min = guess_number     # set the new min
    elif secret_number < guess_number :
         result = 'high'
         num_max = guess_number     # set the new max
    else:
         result = 'bingo'  
    

    guess_list.append([guess_time,newAI,result,y_pos])
    done_list = guess_list

    # if result == 'bingo':
    #      for i in range(len(guess_list)-1):
    #           guess_list.pop(i)

    #      return result


def draw(canvas):
    global result,guess_list,guesses,y_pos,guesses
    
    for guesses in guess_list :
        
        if guesses[2] == 'low' :
            canvas.draw_text(str(guesses[1])+"? Nope~ Should be a higher one.",(10,guesses[3]),12,"black")
        elif guesses[2] == 'high' :
            canvas.draw_text(str(guesses[1])+"? Nope~ Should be a lower one." ,(10,guesses[3]),12,"black")
        elif guesses[2] == 'bingo':
            canvas.draw_text("\(^o^)/~ Bingo!! "+ str(guesses[1]) ,(10,guesses[3]),12,"black")
            canvas.draw_text("Your guess history:"+str(guess_list) ,(10,guesses[3]+30),12,"black")
           # timer.stop()
            return
        #else:
        #    canvas.draw_text("Welcome~" ,(10,guesses[3]),12,"black")
 


def replayStep():
    global guess_list,done_list,guess_time,newAI,result,step

    guess_list = [] # empty the list

    if step < guess_time :
        for i in range(0,step):
            guess_list.append(done_list[step])
        step += 1
    else:
        step = 0

def replay():
    if timer.is_running() :
        timer.stop()
    else:
        timer.start()

def stop():
    timer.stop()

# create frame
frame = simplegui.create_frame('Guess the number', 300, 300)
frame.set_canvas_background("White")
frame.set_draw_handler(draw)

# create UI elements
frame.add_label('Welcome to the game!')
frame.add_label('')
frame.add_button('start',range100,200)
frame.add_label('')
frame.add_button('step by step guess',compare,200)
#frame.add_input('Take a guess (integer only please)', compare, 200)
frame.add_button('replay',replay,200)
frame.add_button('stop',stop,200)

timer = simplegui.create_timer(interval,replayStep)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
#new_game()


# always remember to check your completed program against the grading rubric
