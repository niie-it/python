# Nhập thông tin sinh viên
ho_ten = input("Họ tên: ")
ma_so_sv = input("Mã số sinh viên: ")
email = input("Email: ")
dia_chi = input("Địa chỉ: ")

# Ghi xuống file, vd: datasv.txt
filename = "datasv.txt"
output_data = [ho_ten, ma_so_sv, email, dia_chi]
with open(filename, "w", encoding="utf8") as myfile:
    myfile.write("\n".join(output_data))
    
# Đọc dữ liệu lên
with open(filename, "r", encoding="utf8") as myfile:
    print(myfile.read())