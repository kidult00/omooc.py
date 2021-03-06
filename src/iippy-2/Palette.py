# Palette

#import simplegui
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import urllib2
import codeskulptor

# intialize globals
ShapeType = "circle"
ShapeColor = "green"
Radius = 15
shape_list = []
history_list = []
clickCount = 0
step = 0
interval = 500


# helper function 
     
# define event handlers for shapes

def draw_circle():
    global ShapeType
    ShapeType = "circle"

def draw_triangle():
    global ShapeType
    ShapeType = "triangle"

def draw_square():
    global ShapeType
    ShapeType = "square"

# define event handlers for color

def draw_green():
    global ShapeColor
    ShapeColor = "green"

def draw_blue():
    global ShapeColor
    ShapeColor = "blue"

def draw_red():
    global ShapeColor
    ShapeColor = "red"


# define event handlers for click & draw & reset

def mouseclick(pos):
    global ShapeType,ShapeColor,shape_list,history_list,Radius,clickCount
    
    # if replaying, jump out
    if timer.is_running():
        return

    x = pos[0]
    y = pos[1]

    # decide which shapetype and log the position
    if ShapeType == "circle":
        pos = [x,y]
    elif ShapeType == "triangle":
        pos = [(x, y - Radius),(x + 2*Radius, y + Radius),(x - 2*Radius, y + Radius)]
    elif ShapeType == "square":
        pos = [(x - Radius , y - Radius),(x + Radius , y - Radius),(x + Radius , y + Radius),(x - Radius , y + Radius)]

    # count the drawings
    if clickCount < 1024 :
        shape_list.append([pos,ShapeType,ShapeColor])
        clickCount += 1

    print pos
    print shape_list

    history_list = shape_list   # make a copy before shape_list is modified


def draw(canvas):
    global shapes,shape_list,Radius,clickCount,interval
    
    for shapes in shape_list:
        if shapes[1] == "circle":
            canvas.draw_circle(shapes[0],Radius, 1, "Black",shapes[2])
        else:
            canvas.draw_polygon(shapes[0], 1, "Black",shapes[2])
    
    # give the count on the canvas
    if clickCount == 0:
        canvas.draw_text("Draw shapes below :)",(10,15),12,"black")
    elif clickCount ==1:
        canvas.draw_text("You've drawed "+str(clickCount)+" shape" ,(10,15),12,"black")
    else:
        canvas.draw_text("You've drawed "+str(clickCount)+" shapes" ,(10,15),12,"black")

    if interval !=500:
        canvas.draw_text("Replay interval is:"+str(interval)+"ms" ,(10,30),12,"black")


 
# define event handlers for timer

def replayStep():   #key func of replay
    global step,clickCount,shape_list,history_list
    #step = 0  #step can't be local. it should inscrease after each timer interval

    shape_list = [] # empty the list

    if step < clickCount :  # if replay steps are less than drawings
        step += 1
        for history_step in range(0,step):  # for all in replay steps
        #    if step <= clickCount :
                shape_list.append(history_list[history_step])   # add history[step]
    else:
        step = 0    #if replay steps >= drawings, then start from 0


def replay():
    timer.start()

def stop():
    timer.stop()

def speedup():
    global interval,timer
    if timer.is_running():
        timer.stop()
        interval = interval/2
        timer = simplegui.create_timer(interval,replayStep)
        timer.start()

def slowdown():
    global interval,timer
    if timer.is_running():
        timer.stop()
        interval = interval*2
        timer = simplegui.create_timer(interval,replayStep)
        timer.start()


# create frame and controls
frame = simplegui.create_frame("Palette", 500, 500)
frame.set_canvas_background("White")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
# register event handlers for shape
frame.add_label("请选择形状：\n",200)
frame.add_button("圆形\n",draw_circle,100)
frame.add_button("三角形\n",draw_triangle,100)
frame.add_button("正方形\n",draw_square,100)
# register event handlers for color
frame.add_label("请选择颜色：\n",200)
frame.add_button("绿色\n",draw_green,100)
frame.add_button("蓝色\n",draw_blue,100)
frame.add_button("红色\n",draw_red,100)
#color_r = frame.add_input('R', rgb_r, 50)
#color_g = frame.add_input('G', rgb_g, 50)
#color_b = frame.add_input('B', rgb_b, 50)
frame.add_label(" ",100)
# register event handlers for replay
frame.add_label("回放绘制记录：\n",200)
frame.add_button("开始\n",replay,100)
frame.add_button("暂停\n",stop,100)
frame.add_button("加快一倍\n",speedup,100)
frame.add_button("减慢一半\n",slowdown,100)
# register event handlers for reset
#frame.add_label("",200)
#frame.add_button("重置\n",reset,100)

timer = simplegui.create_timer(interval,replayStep)

# get things rolling
frame.start()


# Always remember to review the grading rubric