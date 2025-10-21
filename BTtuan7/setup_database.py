# 32 tái sử dụng các hàm

def create_username (first_name, last_name):
    #tên người dùng bao gồm chữ cái đầu tiên của tên và họ
    username = first_name[0]+last_name

    #chuyển về chữ in thường
    username = username.lower()
    return username
    
import random

def create_password():
    #tạo mật khẩu gồm 4 số nguyên ngẫu nhiên
    password = str(random.randint(1000,9999))

    return password

def create_database (customer):
    db = {} # từ điển
    # cho từng khách hàng
    for khach in customer:
        # tạo username
        username = create_username(khach[0],khach[1])

        #tạo pass
        password = create_password()

        # lưu 2 biến trên vào db
        db[username] = password
    n_customers = len(db)
    return db,n_customers
