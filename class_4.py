#文字內容
from tkinter import *
root = Tk()
root.title("title1")
label =Label(root,text="i like tkinter")
label.pack()#包裝與定位
print(type(label))#回傳

root.mainloop()