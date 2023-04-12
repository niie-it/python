from tkinter import *

root = Tk()
root.title("DEMO ABC")
root.geometry("400x300")

Label(
    root,
    bg="green yellow", #Màu nền
    font="Arial 14",
    text="First name",
    fg="red", # Màu chữ    
).grid(row=0, column=0)
firstname = Entry(root)
firstname.grid(row=0, column=1)

Label(root, text="Last name").grid(row=1, column=0)
lastname = Entry(root)
lastname.grid(row=1, column=1)

from tkinter import messagebox
def handleShow():
    messagebox.showinfo("Thông tin", 
        f"Hello {firstname.get()} {lastname.get()}")
    
Button(root, text="Show", command=handleShow).grid(row=2, column=1)
Button(root, text="Quit", command=root.quit).grid(row=2, column=0)

root.mainloop()