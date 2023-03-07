chuoi = input("Nhập chuỗi")
print("Chuỗi vừa nhập:", chuoi)

# Loại bỏ ký tự thừa
chuoi = chuoi.replace(",", "")
# Tách chuỗi thành mảng
mang_chuoi = chuoi.split()
print(mang_chuoi)

my_dict = {}
# duyệt qua từng phần tử trong mang_chuoi và đếm số lần xuất hiện
for item in mang_chuoi:
    my_dict[item] = mang_chuoi.count(item)

print(my_dict)