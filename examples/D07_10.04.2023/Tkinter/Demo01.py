from tkinter import *
from tkinter import ttk

# Tạo cửa sổ chính (form chính)
main = Tk()

# setup form chính
main.title("21BITV03")

# Thêm control lên giao diện
lblTieuDe = Label(main, text="Hello Advanced Programmer")
lblTieuDe.pack() #sắp xếp control vô layout
btnSay = Button(main, text="Say Hello")
btnSay.pack()

img = PhotoImage(file="niie.png")
Label(main, image=img).pack()

# Hiện form
main.mainloop()