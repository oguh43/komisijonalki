
from tkinter import *

x = int(input("X: "))
y = int(input("Y: ")) #chyba v zadaní, raz je tam y, raz z
r = int(input("R: "))
k = int(input("K: "))

#x,y,r,k = 190,130,120,6


c = 1


root = Tk()
root.title("Platňa")

canvas = Canvas(root, width="500", height="500")
canvas.pack()

while r >= 15:
    c = c - 1
    canvas.create_oval(x-r,y-r, x+r,y+r, outline="grey" if c == 0 else "black")
    r = r - 3
    if c == 0:
        c = k



root.mainloop()


