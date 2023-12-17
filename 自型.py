from tkinter import *
Reliefs = ["flat","groove","raised","ridge","solid","sunken"]
root = Tk()
for i in Reliefs:
    Label(root,text=i,relief=i,
          fg="blue",
          font="Times 20 bold").pack(side=LEFT,padx=5)
    
root.mainloop()