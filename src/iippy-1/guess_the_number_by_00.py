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

#global variable
secret_number = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0, 100)
    print "Welcome~"
#for test	
#    print secret_number 


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    secret_number = random.randrange(0, 100)
    print "New game? Welcome~"
    print ""
#for test
#    print secret_number 

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    secret_number = random.randrange(0, 1000)
    #for test
    print "New game? Welcome~"
    print ""
#    print secret_number 
    
def input_guess(guess):
    global secret_number
    
    if guess.isdigit():
        number_input = int(guess)
        print "Your guess was: ",number_input
        if secret_number > number_input :
            print "Nope!Higher!"
            print ""
        elif secret_number < number_input :
            print "Nope!Lower!"
            print ""
        else:
            print "\(^o^)/~ Bingo!!"
            print ""
    else:    
        print "Please input an integer!"

    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# create UI elements
frame.add_label('Welcome to the game!')
frame.add_label('')
frame.add_button('Take a [0,100) guess',range100,200)
frame.add_label('')
frame.add_button('Take a [0,1000) guess',range1000,200)
frame.add_label('')
frame.add_input('Take a guess (integer only please)', input_guess, 200)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
