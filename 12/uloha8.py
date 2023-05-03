from random import randint
from tkinter import *

n = int(input("N: "))

nx, Nx, ny, Ny, x, y = 999, 0, 999, 0, 0, 0
# n = najmenšie
# N = najväčšie

root = Tk()
root.title("Obdĺžničok")

canvas = Canvas(root, width="500", height="500")
canvas.pack()

for _ in range(n):
    x = randint(100, 350)
    y = randint(100, 350)
    canvas.create_oval(x-5,y-5,x+5,y+5, fill="red")
    if x < nx:
        nx = x
    if x > Nx:
        Nx = x
    if y < ny:
        ny = y
    if y > Ny:
        Ny = y

canvas.create_rectangle(nx, ny, Nx, Ny, outline="blue")

root.mainloop()


