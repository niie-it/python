import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='python21bitv03',
                             cursorclass=pymysql.cursors.DictCursor)


with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM loai")
    loai_data = cursor.fetchall()
    
    for item in loai_data:
        print(item)
        print(item["MaLoai"], item["TenLoai"])
    
