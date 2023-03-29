import json

def menu():
    print("1. Danh sách sinh viên")
    print("2. Thêm sinh viên")
    print("0. Thoát")
    
    return int(input("Bạn chọn: "))

def doc_ds_sinh_vien():
    with open("StudentManagement.json", "r", encoding="utf8") as myfile:
        mydata = json.load(myfile)
        return mydata
    
if __name__ == "__main__":
    while True:
        chon_lua = menu()
        students = []
        if chon_lua == 0:
            print("Bye bue")
            break
        elif chon_lua == 1:
            students = doc_ds_sinh_vien()
            
        print(f"haha - Chọn {chon_lua}")