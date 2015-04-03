# Palette

import simplegui
#import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

# intialize globals
ShapeType = "circle"
ShapeColor = "green"
Radius = 15
shape_list = []
clickCount = 0
Interval = 500


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

def draw_green():
    global ShapeColor
    ShapeColor = "green"

def draw_blue():
    global ShapeColor
    ShapeColor = "blue"

def draw_red():
    global ShapeColor
    ShapeColor = "red"


def mouseclick(pos):
    global ShapeType,ShapeColor,shape_list,Radius,clickCount
    
    x = pos[0]
    y = pos[1]

    if ShapeType == "circle":
        pos = [x,y]
    elif ShapeType == "triangle":
        pos = [(x, y - Radius),(x + 2*Radius, y + Radius),(x - 2*Radius, y + Radius)]
    elif ShapeType == "square":
        pos = [(x - Radius , y - Radius),(x + Radius , y - Radius),(x + Radius , y + Radius),(x - Radius , y + Radius)]

    print pos

    if clickCount < 1024 :
        shape_list.append([pos,ShapeType,ShapeColor])
        clickCount += 1

    print shape_list

def draw(canvas):
    global ShapeType,ShapeColor,shape_list,Radius
    for shapes in shape_list:
        if shapes[1] == "circle":
            canvas.draw_circle(shapes[0],Radius, 1, "Black",shapes[2])
        else:
            canvas.draw_polygon(shapes[0], 1, "Black",shapes[2])

    canvas.draw_text(str(clickCount)+"st click" ,(10,10),12,"black")
 

def replayStep():
    global clickCount,Radius
    if clickCount > 0 :
        if shape_list[clickCount-1][1] == "circle":
            canvas.draw_circle(shape_list[clickCount],Radius,1,"Black",shape_list[clickCount][2] )
        else :
            canvas.draw_polygon(shape_list[clickCount],1,"Black",shape_list[clickCount][2] )
        clickCount -= 1

def replay():
    timer.start()


def stop():
    timer.stop()

# create frame and controls
frame = simplegui.create_frame("Palette", 500, 500)
frame.set_canvas_background("White")



# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
frame.add_button("圆形\n",draw_circle,100)
frame.add_button("三角形\n",draw_triangle,100)
frame.add_button("正方形\n",draw_square,100)

frame.add_button("绿色\n",draw_green,100)
frame.add_button("蓝色\n",draw_blue,100)
frame.add_button("红色\n",draw_red,100)

frame.add_button("回放\n",replay,100)
frame.add_button("停止\n",stop,100)

timer = simplegui.create_timer(500,replayStep）

# get things rolling
frame.start()


# Always remember to review the grading rubric