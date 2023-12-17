from tkinter import *
root =Tk()
root.title("會員登入")
mamel = Label(root,text="Name ")
mamel.grid(row=0)
addresse = Label(root,text="Addresse ")
addresse.grid(row=1)

name = Entry(root)
addres = Entry(root)
name.grid(row=0,column=1)
addres.grid(row=1 , column =1)

root.mainloop()