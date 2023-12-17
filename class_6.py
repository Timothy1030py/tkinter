#wraplength換行
from tkinter import *
root = Tk()
root.title("title1")
label =Label(root,text="i like tkinter",fg="blue",bg="yellow",height=3,width=15,anchor="nw",
             wraplength=40)#元素超過40自動換行
label.pack()
print(type(label))

root.mainloop()