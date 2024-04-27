import tkinter as tk
from tkinter import ttk 
import time
import math
e = 0
balley = 0
ballex = 0
class Line(tk.Tk):
    def __init__(self, x1, y1, x2, y2, canvas):

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.canvas = canvas
    def create_lines(self):
        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill = "black")
    def remove_line(self):
        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill = "white")

class Ball(tk.Tk):
    def __init__(self, x1, y1, x2y2, canvas, xv, yv, lines):
        self.xv = xv
        self.yv = yv
        self.x1 = x1 
        self.y1 = y1 
        self.x2y2 = x2y2
        self.canvas = canvas
        self.lines = lines
    def create_ball(self):
        self.ball_id = self.canvas.create_oval(self.x1, self.y1, self.x2y2 + self.x1, self.x2y2 + self.y1, outline = "black")
    def remove_ball(self):
        self.canvas.create_oval(self.x1, self.y1, self.x2y2 + self.x1, self.x2y2 + self.y1, fill = "white", outline = "white")
    def check_collision(self):
        for element in lines:
            if element.x1 == element.x2:
                if self.x1 <= element.x1 <= self.x1 + self.x2y2 and \
                ((self.y1+self.x2y2>=element.y1 and self.y1 <= element.y2)or(self.y1+self.x2y2<=element.y1 and self.y1>=element.y2)):
                    self.xv = -self.xv
            if element.y1 == element.y2:
                if self.y1 <= element.y1 <= self.y1 + self.x2y2 and \
                ((self.x1+self.x2y2>=element.x1 and self.x1 <= element.x2)or(self.x1+self.x2y2<=element.x1 and self.x1>=element.x2)):
                    self.yv = -self.yv
    def move_ball(self):  
        self.canvas.move(self.ball_id, self.xv, self.yv)
        self.y1 += self.yv
        self.x1 += self.xv
        self.check_collision()

class Hole(tk.Tk):
    def __init__(self, x1, y1, x2y2, canvas, ball):
        self.x1 = x1
        self.y1 = y1
        self.x2y2 = x2y2
        self.canvas = canvas
        self.ball = ball
        self.e = 0
    def create_hole(self):
        self.canvas.create_oval(self.x1, self.y1, self.x2y2 + self.x1, self.x2y2 + self.y1, fill = "black")
    def ball_collide(self):
        if (self.x1 <= (self.ball.x1 + (self.ball.x2y2/2))<= self.x1 + self.x2y2):
            self.ball.remove_ball()
            self.create_hole()
            self.canvas.update()
            self.e = 1
            self.ball.yv = 0
            self.ball.xv = 0
        else:
            self.e = 0
root = tk.Tk()
root.geometry("500x500")
root.minsize(500,500)
root.resizable(False, False)

canvas = tk.Canvas(root, width = 600, height = 300, bg="white")
canvas.pack()
line = Line(20, 10, 20, 250, canvas)
line.create_lines()
line1 = Line(20, 10, 200, 10, canvas)
line1.create_lines()
line2 = Line(200, 10, 200, 80, canvas)
line2.create_lines()
line3 = Line(200, 80, 70, 80, canvas)
line3.create_lines()
line4= Line(70, 80, 70, 250, canvas)
line4.create_lines()
line5 = Line(70, 250, 20, 250, canvas)
line5.create_lines()
line6 = Line(600, 0, 600, 300, canvas) 
line8 = Line(600, 0, 600, 300, canvas)  
line9 = Line(600, 0, 600, 300, canvas)  
line10 = Line(600, 0, 600, 300, canvas)  
lines = [line, line1, line2, line3, line4, line5, line6, line8, line9, line10]  
x_vel =0 
y_vel =-5  
ball1 = Ball(40, 220, 10, canvas, x_vel, y_vel, lines)  
ball1.create_ball()  
canvas.pack()  
label = tk.Label(root, text = "Power: Defualt")  
label.pack()  
line7 = Line(45, 225, 45, 200, canvas) 
line7.create_lines()  
hole = Hole(160, 40, 10, canvas, ball1)  
hole.create_hole()  
power = tk.Entry(root)  
power.pack()  
angle = (100*math.pi)  
def power_get():  
    power1 = int(power.get())  
    if 0< power1 <= 100:  
        ball1.yv = -(line7.y1 - line7.y2)/(100/(power1))  
        ball1.xv = -(line7.x1 - line7.x2)/(100/(power1))
        label.config(text = f"power: {power1}")
bpower = tk.Button(root, text = "Power", command = power_get) 
bpower.pack()
holes = 0  
def create_hole():  
    global holes  
    global lines
    global hole

    if holes == 1:
        canvas.delete("all")
        time.sleep(1)
        root.update()
        line = Line(600, 0, 600, 300, canvas)
        line1 = Line(600, 0, 600, 300, canvas)
        line2 = Line(600, 0, 600, 300, canvas)
        line3 = Line(600, 0, 600, 300, canvas)
        line4 = Line(600, 0, 600, 300, canvas)
        line5 = Line(600, 0, 600, 300, canvas)
        line6 = Line(600, 0, 600, 300, canvas)
        line8 = Line(600, 0, 600, 300, canvas)
        line9 = Line(600, 0, 600, 300, canvas)
        line10 = Line(600, 0, 600, 300, canvas)
        line = Line(20, 10, 20, 250, canvas)
        line1 = Line(20, 10, 250, 10, canvas)  
        line2 = Line(250, 10, 250, 40, canvas) 
        lines = [line, line1, line2, line3, line4, line5, line6, line8, line9, line10]
        for element in lines:  
            element.create_lines()  
        root.update()
def li():  
    line7.remove_line()  
    ball1.remove_ball()  
def bind_bm(event):
    print(ball1.yv)
    global angle
    global line7
    global lines
    global balley
    global ballex
    global holes
    print(angle)
    if  angle % (2*math.pi) == 0:
        ball1.yv = -5  
    true_v = True  
    line7.remove_line()  
    ball1.remove_ball()  
    for element in lines:  
        element.create_lines()  
    qw = 0
    i = 0
    while true_v:  
        if ball1.yv < 0:  
            balley = -ball1.yv 
        else:  
            balley = ball1.yv  
        if ball1.xv < 0: 
            ballex = -ball1.xv  
        else:  
            ballex = ball1.xv  
        qw += 0.1  
        ball1.move_ball()  
        root.update()  
        time.sleep(0.02 + i)  
        i+=0.01  
        balley -= qw  
        ballex -= qw 
        if ball1.yv < 0:  
            ball1.yv = -balley 
        else:  
            ball1.yv = balley 
        if ball1.xv < 0: 
            ball1.xv = -ballex  
        else:  
            ball1.xv = ballex

        hole.ball_collide()
        if balley <= 0 and ballex <= 0:
            true_v = False
    abc = 1
    if hole.e != 1:
        ball1.create_ball()
    else:
        canvas.delete("all")
        canvas.update()
        abc = 0
    line7 = Line((ball1.x1+(ball1.x2y2/2)),
    (ball1.y1+(ball1.x2y2/2)),
    (ball1.x1+(ball1.x2y2/2)),
    (ball1.y1+(ball1.x2y2/2))-20, canvas)
    line7.create_lines()
    angel  =(100*math.pi)
    ball1.yv = -5
    if abc == 0:
        canvas.delete("all")
        holes += 1
        create_hole()

def change_linangl(event):
    global angle
    ball1.yv = -5
    global line7
    global lines
    global hole
    time.sleep(0.1)
    angle += math.pi/20
    angle = angle % 360
    line7.remove_line()
    line7 = Line((ball1.x1+(ball1.x2y2/2)),
    (ball1.y1+(ball1.x2y2/2)),
    ((ball1.x1+(ball1.x2y2/2))-(math.sin(angle)*20)),
    ((ball1.y1+(ball1.x2y2/2))-(math.cos(angle)*20)), canvas)
    line7.create_lines()
    hole.create_hole()
    ball1.create_ball()
    for element in lines:
        element.create_lines()
def change_linangr(event):
    global angle
    ball1.yv = -5
    global line7
    global lines
    global hole
    time.sleep(0.1)
    angle -= math.pi/20
    if angle < 0:
        angle += (math.pi*20)
    angle = angle % 360
    line7.remove_line()
    line7 = Line((ball1.x1+(ball1.x2y2/2)),
    (ball1.y1+(ball1.x2y2/2)),
    ((ball1.x1+(ball1.x2y2/2))-(math.sin(angle)*20)),
    ((ball1.y1+(ball1.x2y2/2))-(math.cos(angle)*20)), canvas)
    line7.create_lines()
    hole.create_hole()
    ball1.create_ball()
    for element in lines:
        element.create_lines()




canvas.bind("<Button-1>",bind_bm)
root.bind("<KeyPress-a>",change_linangl)
root.bind("<KeyPress-d>",change_linangr)





root.mainloop()