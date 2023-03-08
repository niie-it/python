'''
Viết hàm chào bạn X với X nhập từ bàn phím
'''

def chao(ten):
    print(f"xin chào bạn {ten}")
    
# Demo
chao("Lan")
chao("Diep")
ten = input("Nhập tên bạn: ")
chao(ten)