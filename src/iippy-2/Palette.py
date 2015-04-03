# Palette

import simplegui
#import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

# intialize globals
ShapeType = "circle"
Radius = 15
shape_list = []


# helper function
     
# define event handlers

def draw_circle():
    global ShapeType
    ShapeType = "circle"

def draw_triangle():
    global ShapeType
    ShapeType = "triangle"

def draw_square():
    global ShapeType
    ShapeType = "square"


def mouseclick(pos):
    global ShapeType,shape_list,Radius
    
    x = pos[0]
    y = pos[1]

    if ShapeType == "circle":
        pos = [x,y]
    elif ShapeType == "triangle":
        pos = [(x, y - Radius),(x + 2*Radius, y + Radius),(x - 2*Radius, y + Radius)]
    elif ShapeType == "square":
        pos = [(x - Radius , y - Radius),(x + Radius , y - Radius),(x + Radius , y + Radius),(x - Radius , y + Radius)]

    print pos

    shape_list.append([pos,ShapeType])

def draw(canvas):
    global ShapeType,shape_list,Radius
    for shapes in shape_list:
        if shapes[1] == "circle":
            canvas.draw_circle(shapes[0],Radius, 1, "Black")
        else:
            canvas.draw_polygon(shapes[0], 1, "Black")
 

# create frame and controls
frame = simplegui.create_frame("Palette", 500, 500)
frame.set_canvas_background("White")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
frame.add_button("圆形\n",draw_circle,100)
frame.add_button("三角形\n",draw_triangle,100)
frame.add_button("正方形\n",draw_square,100)

# get things rolling
frame.start()


# Always remember to review the grading rubric