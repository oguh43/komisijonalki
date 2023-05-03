
from tkinter import *
from random import randint


root = Tk()
root.title("Prečo :(")

canvas = Canvas(root, width="500", height="500")
canvas.pack()
offset = 0
for _ in range(10000):
    x = randint(10, 350)
    y = randint(10, 230)
    offset = ((y * 2) - 10)/1.75
    if y < 120:
        if x > offset:
            canvas.create_oval(x-5,y-5,x+5,y+5, fill="white")
        else:
            canvas.create_oval(x-5,y-5,x+5,y+5, fill="blue")
    else:
        offset = 130-(((y-120) * 2) - 10)/1.75
        if x > offset:
            
            canvas.create_oval(x-5,y-5,x+5,y+5, fill="red")
        else:
            canvas.create_oval(x-5,y-5,x+5,y+5, fill="blue")


root.mainloop()
