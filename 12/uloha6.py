
from tkinter import *


root = Tk()
root.title("Obloha")

canvas = Canvas(root, width="500", height="500", highlightthickness=1, highlightbackground="blue")
canvas.pack()
x = 450
num = int(input("Číselko: "))
while num!=0:
    canvas.create_rectangle(x, 200, x-20, 180, fill="cyan")
    canvas.create_text(x-10, 190, text=num%10)
    x = x - 23
    num = num // 10


root.mainloop()


