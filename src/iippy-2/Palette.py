# Palette

import simplegui
#import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

# intialize globals
ball_pos = [250,250]
BALL_RADIUS = 15


# helper function
     
# define event handlers

def mouseclick(pos):
	global ball_pos
    ball_pos = list(pos)

def draw(canvas):
	canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Black")

# create frame and controls
frame = simplegui.create_frame("Palette", 500, 500)
frame.set_canvas_background("White")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
frame.start()


# Always remember to review the grading rubric