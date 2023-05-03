
# bez random
"""from tkinter import *

cas = int(input("Zadaj cas: "))



root = Tk()
root.title("Obloha")

canvas = Canvas(root, width="500", height="500")
canvas.pack()

if cas < 8:
    canvas.configure(bg='blue')
    canvas.create_oval(150,50,250,150, fill="white")
else:
    canvas.configure(bg='cyan')
    canvas.create_oval(150,50,250,150, fill="yellow")


root.mainloop()"""

# s random
from tkinter import *
from random import randint

cas = int(input("Zadaj cas: "))
x = randint(50, 450)
y = randint(50, 450)

root = Tk()
root.title("Obloha")

canvas = Canvas(root, width="500", height="500")
canvas.pack()

if cas < 8:
    canvas.configure(bg='blue')
    canvas.create_oval(x-50,y-50,x+50,y+50, fill="white")
else:
    canvas.configure(bg='cyan')
    canvas.create_oval(x-50,y-50,x+50,y+50, fill="yellow")


root.mainloop()


