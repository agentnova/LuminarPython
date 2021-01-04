from tkinter import *

root = Tk()
frameTop = Frame(root)
frameTop.pack()
frameBottom = Frame(root)
frameBottom.pack()

button1 = Button(frameTop, text="btn1", fg="red")
button2 = Button(frameTop, text="btn2", fg="green")
button3 = Button(frameTop, text="btn3", fg="yellow")
button4 = Button(frameBottom, text="btn4", fg="cyan")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()
