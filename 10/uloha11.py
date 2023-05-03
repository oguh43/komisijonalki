
from tkinter import *



root = Tk()
root.title("Obloha")

canvas = Canvas(root, width="1000", height="200")
canvas.pack()

for i in range(0,15):#8
    canvas.create_oval(50+i*50,50,100+i*50,100, fill="red" if i <8 else "blue")


root.mainloop()


