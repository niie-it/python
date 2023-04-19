from DbUtils import DbUtil

dsloai = DbUtil.get_data("SELECT * FROM Loai")
for item in dsloai:
    print(item)


print("INSERTING>>>>>>")
sql_insert = f"INSERT INTO Loai(TenLoai) VALUES('Trí Thức')"
if DbUtil.change_data(sql=sql_insert):
    print('Thêm thành công!')

dsloai = DbUtil.get_data("SELECT * FROM Loai")
for item in dsloai:
    print(item)
