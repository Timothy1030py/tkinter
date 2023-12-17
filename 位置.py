from tkinter import *

root = Tk()
root.title("hello")
root.geometry("300x180")
ok = Label(root,text="ok",
           font = "Times 20 bold",
           fg="white",bg = "blue")

ok.pack(anchor=S,side=RIGHT,
        padx=10,pady=10)

root.mainloop()