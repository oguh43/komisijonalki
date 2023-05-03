
from tkinter import *

a = int(input("Zadaj cislo r1: "))
b = int(input("Zadaj cislo r2: "))

c = 0
if b > a:
    c = a
    a = b
    b = c

root = Tk()
root.title("Obloha")

canvas = Canvas(root, width="500", height="500")
canvas.pack()

canvas.create_oval(250-a/2,500-a,250+a/2,500, fill="blue")
canvas.create_oval(250-b/2,500-a-b,250+b/2,500-a, fill="blue")



root.mainloop()


