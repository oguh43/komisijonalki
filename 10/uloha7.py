
from tkinter import *

a = int(input("Zadaj cislo a: "))
b = int(input("Zadaj cislo b: "))

c = 0
if b > a:
    c = a
    a = b
    b = c

root = Tk()
root.title("Obloha")

canvas = Canvas(root, width="500", height="500")
canvas.pack()

canvas.create_rectangle(250-a/2,500-b,250+a/2,500, fill="red")

root.mainloop()


