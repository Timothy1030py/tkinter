from tkinter import *

def msgShow():
    label.config(text="Swift",bg="lightyellow",fg="pink")
root = Tk()
root.title("what do you love")
label = Label(root)
btn = Button(root,text="列印訊息",command=msgShow)
label.pack()
btn.pack()

root.mainloop()