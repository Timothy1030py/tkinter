from tkinter import *

def msgShow():
    label.config(text="Swift",bg="lightyellow",fg="red")
root = Tk()
root.geometry("300x300")
root.title("what do you love")
label = Label(root)
btn = Button(root,text="列印訊息",width=15,command=msgShow)
end = Button(root,text="結束",width=15,command=root.destroy)
label.pack()
btn.pack()
end.pack()
root.mainloop()