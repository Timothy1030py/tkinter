from tkinter import *
counter = 0
def run_counter(digit):
    def counting():
        global counter
        counter+=1
        digit.config(text = str(counter))
        digit.after(1000,counting)
    counting()
root = Tk()
root.title("hello")
digit = Label(root,bg="yellow",fg="blue",
              height=3,width=10,font="Helvetica 20 ")
digit.pack()
run_counter(digit)
root.mainloop()