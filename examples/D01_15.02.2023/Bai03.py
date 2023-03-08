# Bài 3: ATM (unlimited)
so_tien_can_rut = int(input("Nhập tiền cần rút: "))

so_to_50k = so_tien_can_rut // 50
tmp = so_tien_can_rut % 50

so_to_20k = tmp // 20
tmp = tmp % 20

so_to_5k = tmp // 5
tmp = tmp % 5

print(f"Đổi {so_tien_can_rut} = {so_to_50k} x 50k + {so_to_20k} x 20k + {so_to_5k} x 5k")

