from Diem import Point
A = Point()
A.x = 7
A.y = 5
A.name = "A"
B = Point()
B.x = 9
B.y = -11
B.name = "Pi"

mang = []
mang.append(A)
mang.append(B)

C = Point("CC", 11, -101)
mang.append(C)
mang.append(Point("D"))
mang.append(Point("E", 999))


# print(A)
for item in mang:
    # item.display()
    print(item)
    
#Demo distance AB
print(A.distance(B))
print(B.distance(A))