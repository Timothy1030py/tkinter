from tkinter import *
from tkinter.ttk import Separator

root = Tk()
root.title("分割線")
myTitle = "美好的一天"
lab1 = Label(root,text=myTitle,font="Helvetic 20 bold")
lab1.pack(padx=10,pady=10)

sep = Separator(root,orient = HORIZONTAL)
sep.pack(fill=X, pady=5)

lab2 = Label(root,text=myTitle)
lab2.pack(padx=10 , pady=10)

root.mainloop()