'''
Bài tập tăng tốc

- Nhập N số nguyên dương
- Nhập mảng N giá trị nguyên
- Tìm số lớn nhất

Hint:
	mảng python ==> dùng list
	khai báo mảng rỗng:
		A = [] # A = list()
	thêm 1 phần tử item vào mảng:
		A.append(item)
'''
N = int(input("Nhập số phần tử: "))

A = []

for i in range(N):
    tmp = int(input(f"Nhập giá trị phần tử thứ {i+1}: "))
    A.append(tmp)


print(f"Số lượng phần tử: {len(A)}")    
print(f"Giá trị lớn nhất là: {max(A)}")