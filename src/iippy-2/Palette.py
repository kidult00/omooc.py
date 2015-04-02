# Palette

import simplegui
#import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

# intialize globals
circle_pos = [250,250]
triangle_1 = [0,0]
triangle_2 = [0,0]
triangle_3 = [0,0]
BALL_RADIUS = 15
tri_height = 10


# helper function
     
# define event handlers

def mouseclick(pos):
    global circle_pos,triangle_pos,triangle_1,triangle_2,triangle_3
    circle_pos = list(pos)
    x = pos[0]
    y = pos[1]
    triangle_1 = [x, y-tri_height]
    triangle_2 = [x+2*tri_height,y+tri_height]
    triangle_3 = [x-2*tri_height,y+tri_height]
    print "c=",circle_pos
#    print "t=",triangle_pos

def draw(canvas):
    canvas.draw_circle(circle_pos, BALL_RADIUS, 1, "Black")
    canvas.draw_polygon([triangle_1,triangle_2,triangle_3], 1, "Black")


# create frame and controls
frame = simplegui.create_frame("Palette", 500, 500)
frame.set_canvas_background("White")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
frame.start()


# Always remember to review the grading rubric