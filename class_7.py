#wraplength換行
from tkinter import *
root = Tk()
root.title("title1")
label =Label(root,text="i like tkinter",
             fg="blue",bg="lightyellow",
             height=3,width=15,
             anchor="se",
             font="Helvetica 20 bold")#粗體文字
label.pack()
print(type(label))

root.mainloop()