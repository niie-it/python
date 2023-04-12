from tkinter import *

root = Tk()
root.geometry("400x300")

## Nên tách phần này ra file riêng
def mo_man_hinh_login(main):
    # Khai báo màn hình con của main
    login = Toplevel(main)
    login.title("LOGIN PAGE")
    Label(login, text="Username").grid(row=0, column=0)
    Label(login, text="Password").grid(row=1, column=0)
    login.mainloop()
    
## End Nên tách phần này ra file riêng

# Khai báo menu
main_menu = Menu(root)

mnu_he_thong = Menu(main_menu, tearoff=0)
mnu_he_thong.add_command(label="Đăng nhập", command=lambda: mo_man_hinh_login(root))
mnu_he_thong.add_command(label="Đăng xuất")
mnu_he_thong.add_separator()
mnu_he_thong.add_command(label="Thoát", command=root.quit)
main_menu.add_cascade(label="Hệ thống", menu=mnu_he_thong)

mnu_quan_ly = Menu(main_menu, tearoff=0)
mnu_quan_ly.add_command(label="Quản lý Lớp")
mnu_quan_ly.add_command(label="Quản lý Sinh viên")
mnu_quan_ly.add_command(label="Nhập điểm")
main_menu.add_cascade(label="Quản lý", menu=mnu_quan_ly)

# Gắn menu vào màn hình chính
root.config(menu=main_menu)

root.mainloop()