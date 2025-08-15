'''
from tkinter import *
win = Tk()
canvas = Canvas(win, bg = "white", width = 300, height = 300)
canvas.pack()
win.mainloop()

from tkinter import *
win = Tk()
canvas = Canvas(win, bg = "white", width = 500, height = 100)
canvas.create_line(0, 50, 500, 50, fill = "blue", width = 5)
canvas.pack()
win.mainloop()

from tkinter import *
win = Tk()
canvas = Canvas(win, bg = "white", width = 480, height = 480)
canvas.pack()
for i in range(10, 500, 50) :
    x1, y1 = 10,i
    x2, y2 = 460, y1
    canvas.create_line(x1, y1, x2, y2, fill = "blue", width = 5)
    canvas.create_line(y1, x1, y2, x2, fill = "red", width = 5)
win.mainloop()

from tkinter import *
def paint(event) :
    x1,y1 = event.x, event.y
    x2,y2 = x1 + 5, y1 + 5
    canvas.create_line(x1, y1, x2, y2, width = 3)
win = Tk()
canvas = Canvas(win, bg = "white", width = 700, height = 700)
canvas.pack()
win.bind("<B1-Motion>", paint)
win.mainloop()

from tkinter import *
pen_color = "black"
def paint(event) :
    global pen_color
    x1, y1 = event.x, event.y
    x2, y2 = x1 + 5, y1 + 5
    canvas.create_line(x1, y1, x2, y2, width = 3, fill = pen_color)
def change_color() :
    global pen_color
    pen_color = "red"
win = Tk()
canvas = Canvas(win, bg = "white", width = 500, height = 200)
btn = Button(win, text = "red", command = change_color)
canvas.pack()
btn.pack()
win.bind("<B1-Motion>", paint)
win.mainloop()
'''
from tkinter import *
w = 6
pen_size = 2
pen_color = "black"
def paint(event) :
    global pen_size
    x1, y1 = event.x, event.y
    x2, y2 = event.x + pen_size, event.y + pen_size
    canvas.create_line(x1, y1, x2, y2, width = pen_size, fill = pen_color)
def change_color(color) :
    global pen_color
    pen_color = color
def change_size(btn) :
    global pen_size
    if btn == "plus" :
        pen_size += 1
    else :
        if pen_size > 2 :
            pen_size -= 1
def clear_canvas() :
    canvas.delete("all")
win = Tk()
win.title("My paint")
win.geometry("500x500+200+200")
canvas = Canvas(win, width = 500, height = 470, bg = "white")
canvas.bind("<B1-Motion>", paint)
btn_white = Button(win, bg = "white", width = w, command = lambda : change_color("white"))
btn_black = Button(win, bg = "black", width = w, command = lambda : change_color("black"))
btn_blue = Button(win, bg = "blue", width = w, command = lambda : change_color("blue"))
btn_green = Button(win, bg = "green", width = w, command = lambda : change_color("green"))
btn_yellow = Button(win, bg = "yellow", width = w, command = lambda : change_color("yellow"))
btn_red = Button(win, bg = "red", width = w, command = lambda : change_color("red"))
btn_plus = Button(win, text = "+", bg = "white", width = w, command = lambda : change_size("plus"))
btn_minus = Button(win, text = "-", bg = "white", width = w, command = lambda : change_size("minus"))
btn_clear = Button(win, text = "clear", bg = "white", width = w, command = clear_canvas)
canvas.grid(row = 0, column = 0, columnspan = 9)
btn_white.grid(row = 1, column = 0)
btn_black.grid(row = 1, column = 1)
btn_blue.grid(row = 1, column = 2)
btn_green.grid(row = 1, column = 3)
btn_yellow.grid(row = 1, column = 4)
btn_red.grid(row = 1, column = 5)
btn_plus.grid(row = 1, column = 6)
btn_minus.grid(row = 1, column = 7)
btn_clear.grid(row = 1, column = 8)
win.mainloop()
