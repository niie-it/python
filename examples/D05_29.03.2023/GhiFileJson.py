# GhiFileJson.py

# Khai báo dict ==> lưu file json
ds_sinh_vien = [
    {
        "masv": 19001004, "hoTen": "Lý Tèo", "gioiTinh": True
    },
    {
        "masv": 19001824, "hoTen": "Hùng Lê", "gioiTinh": False
    }
]

# dict ==> json: dump
import json
print(json.dumps(ds_sinh_vien, indent=4))

with open("Students.json", "w", encoding="utf8") as myfile:
    json.dump(ds_sinh_vien, myfile, indent=4)