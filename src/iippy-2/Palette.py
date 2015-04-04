# Palette

import simplegui
#import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

# intialize globals
ShapeType = "circle"
ShapeColor = "green"
Radius = 15
shape_list = []
history_list = []
clickCount = 0
step = 0


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

# define event handlers for click & draw

def mouseclick(pos):
    global ShapeType,ShapeColor,shape_list,history_list,Radius,clickCount
    
    x = pos[0]
    y = pos[1]

    # 判断形状并记录位置
    if ShapeType == "circle":
        pos = [x,y]
    elif ShapeType == "triangle":
        pos = [(x, y - Radius),(x + 2*Radius, y + Radius),(x - 2*Radius, y + Radius)]
    elif ShapeType == "square":
        pos = [(x - Radius , y - Radius),(x + Radius , y - Radius),(x + Radius , y + Radius),(x - Radius , y + Radius)]

    # 记录绘制次数
    if clickCount < 1024 :
        shape_list.append([pos,ShapeType,ShapeColor])
        clickCount += 1

    print pos
    print shape_list

    history_list = shape_list   # 后面会修改shape_list，所以需要复制一份list


def draw(canvas):
    global shapes,shape_list,Radius,clickCount
    for shapes in shape_list:
        if shapes[1] == "circle":
            canvas.draw_circle(shapes[0],Radius, 1, "Black",shapes[2])
        else:
            canvas.draw_polygon(shapes[0], 1, "Black",shapes[2])

    # 在画布上显示已点击次数
    canvas.draw_text(str(clickCount)+"st click" ,(10,10),12,"black")

 
# define event handlers for timer

def replayStep():   #控制回放行为的关键函数
    global step,clickCount,shape_list,history_list
    #step = 0  #step不能为局部变量，每次timer完需要加1

    shape_list = [] #清空以便从头开始绘制

    if step < clickCount :  #如果回放步数小于绘制次数
        step += 1
        for history_step in range(0,step):  #对所有回放步数内已保存的记录指针
        #    if step <= clickCount :
                shape_list.append(history_list[history_step])   #往list中添加 历史记录[步数]
    else:
        step = 0    #如果回放步数不小于绘制次数，回放步数归零


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
frame.add_label(" ",100)
# register event handlers for replay
frame.add_label("回放绘制记录：\n",200)
frame.add_button("开始\n",replay,100)
frame.add_button("停止\n",stop,100)

timer = simplegui.create_timer(500,replayStep)

# get things rolling
frame.start()


# Always remember to review the grading rubric