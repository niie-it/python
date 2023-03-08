'''
BMI = W/ [(H)2]
Trong đó:
	BMI đơn vị thường dùng là kg/m2	
	W là cân nặng (kg)
	H là chiều cao (m)
- BMI <16: Gầy độ III
- 16 ≤ BMI <17: Gầy độ II
- 17 ≤ BMI < 18.5: Gầy độ I
- 18.5 ≤ BMI < 25: Bình thường
- 25 ≤ BMI < 30: Thừa cân
- 30 ≤ BMI < 35: Béo phì độ 1
- 35 ≤ BMI < 40: Béo phì độ II
'''
try:
    W = float(input("Nhập cân nặng (kg): "))
    H = float(input("Nhập chiều cao (m): "))
    BMI = W / (H * H)
    print("BMI = ", BMI)

    if BMI < 16:
        print("Gầy độ III")
        print("HAHAHA")
    elif BMI < 17:
        print("Gầy độ II")
    elif BMI < 18.5:
        print("Gầy độ I")
    elif BMI < 25:
        print("Bình thường")
    elif BMI < 30:
        print("Thừa cân")
    elif BMI < 35:
        print("Béo phì độ 1")
    elif BMI < 40:
        print("Béo phì độ 2")
    else:
        print("Béo độ 3")
except:
    print("Có lỗi")