# Đọc từng của file
try:
    myfile = open("data.txt", "r", encoding="utf8")
    
    # for line in myfile:
    #     print(line)
    
    # data = myfile.read()
    # print(data)
    
    lines = myfile.readlines()
    print(lines)
    for line in lines:
        print(line)    
    
    myfile.close()
except Exception as ex:
    print(ex)