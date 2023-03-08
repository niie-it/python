'''
Viết hàm kiểm ra một só có phải là nguyên tố không?
def LaSoNguyenTo(N):
	pass

Xuất ra các số nguyên tố từ 3 ==> 1000000
'''

def LaSoNguyenTo(N):
  if N < 2:
    return False
    
  for i in range(2, N):
    if N % i == 0:
      return False

  return True

# Xuất ra các số nguyên tố từ 3 ==> 1000000
for idx in range(3, 1000001, 2):
    if LaSoNguyenTo(idx):
        print(idx)