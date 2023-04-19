# Định nghĩa lớp làm việc với CSDL
import pymysql

class DbUtil:
    @staticmethod
    def get_connection():
        try:
            return pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='python21bitv03',
                             cursorclass=pymysql.cursors.DictCursor)
        except:
            return None
        
    @staticmethod
    def get_data(sql):
        mycon = DbUtil.get_connection()
        if mycon:
            with mycon.cursor() as cursor:
                try:
                    cursor.execute(sql)
                    return cursor.fetchall()
                except:
                    return []
    
    @staticmethod
    def change_data(sql):
        mycon = DbUtil.get_connection()
        if mycon:
            with mycon.cursor() as cursor:
                try:
                    cursor.execute(sql)
                    mycon.commit()
                    return True
                except:
                    return False