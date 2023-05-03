
from tkinter import *
from random import randint






root = Tk()
root.title("Nemčúri")

canvas = Canvas(root, width="500", height="500")
canvas.pack()
for _ in range(10000):
    x = randint(10, 350)
    y = randint(10, 250)
    if y < 90:
        canvas.create_oval(x-5,y-5,x+5,y+5, fill="black")
    elif y < 170:
        canvas.create_oval(x-5,y-5,x+5,y+5, fill="red")
    else:
        canvas.create_oval(x-5,y-5,x+5,y+5, fill="yellow")


root.mainloop()


