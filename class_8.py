#wraplength換行
from tkinter import *
root = Tk()
root.title("title1")
label =Label(root,text="ilikoekoeketkinter",
             fg="blue",bg="yellow",
             height=3,width=15,
             anchor="nw",
             wraplength=80,
             justify="left")
label.pack()
print(type(label))
root.mainloop()