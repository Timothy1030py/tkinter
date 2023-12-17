import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('jus')
root.geometry("300x200")

img = Image.open('圖1.gif')        # 開啟圖片
tk_img = ImageTk.PhotoImage(img)    # 轉換為 tk 圖片物件

label = tk.Label(root, image=tk_img, width=300, height=300)  # 在 Lable 中放入圖片
label.pack()

root.mainloop()