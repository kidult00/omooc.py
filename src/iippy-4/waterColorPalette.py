#-- coding: utf8 --

#import simplegui
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

# Global Variables

canvas_width = 300
canvas_height = 300
dots = []


# Classes for colors and dots 
# 定义颜色类
class RGBcolor:
    def __init__(self,red,green,blue):
        self.red = red
        self.green = green
        self.blue = blue
        
    def make_html(self):
        return "rgb(" + str(self.red) + "," + str(self.green) + "," + str(self.blue) + ")"
        # 返回:  rgb(123,123,123) 传递参数用

    def __str__(self):
        return "Red:" + str(self.red) + ", Green:" + str(self.green) + ", Blue:" + str(self.blue)
        # 返回:  Red:123, Green:123, Blue:123  查看信息用

    def fade(self):
        self.red += 1
        self.green += 1
        self.red += 1

# 定义点类
class Dot:
    def __init__(self,pos,color,radius,life):
        self.pos = pos
        self.color = color
        self.life = life
        self.radius = radius

    def draw(self,canvas):  # 调用方法的时候记得传canvas
        # Dot 的 color 域，是 RGBcolor 的实例，因而可以调用 RGBcolor 的 make_html 方法
        dotColor = self.color.make_html()
        # 画点的方法
        canvas.draw_circle(self.pos, self.radius, 1, dotColor, dotColor)

    def animate(self):
        self.life -= 1
        if self.radius < 20 :
            self.radius += 0.8

        self.color.fade()


# Event Handlers
        
def draw(canvas): 
    for dot in dots:
        dot.animate()
        dot.draw(canvas)

        # 点的计数器，到 0 后不再绘制
        if dot.life == 0 :
            dots.remove(dot)
 

def click(pos):  
    # 定义 RGBcolor 新实例
    new_color = RGBcolor(random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))
    print new_color
    print "HTML color is " + new_color.make_html()
    print "dots:" , len(dots)+1

    # 每点一下，就新建 Dot 对象并存入 dots[] 中
    dots.append(Dot(pos, new_color, 20, 256))


# Frame

frame = simplegui.create_frame("Water Color Palette", canvas_width, canvas_height) 

# Register Event Handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.set_canvas_background("White")

# Start
frame.start()