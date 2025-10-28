class Product:
    """Lớp đại diện cho 1 sp"""
    #
    
    #---Hàm khởi tạo---
    def __init__(self,name):
        #khởi tạo
        self.name = name
        self.price = 0
        self.discount = 0
        
t_shirt = Product("Feel good")
    
print("-> Thuộc tính của đối tượng t_shirt khi khởi tạo: ")
print("Tên:",t_shirt.name)
print("Giá:",t_shirt.price)
print("Giảm giá:",t_shirt.discount)
    
print("-> Thuộc tính của đối tượng t_shirt sau khi tùy chỉnh: ")
t_shirt.price = 30
print("Giá:",t_shirt.price,"coins")
t_shirt.discount = 4
print("Giảm giá:",t_shirt.discount,"coins")

print("----------------------------------------------------")

lamp = Product("Lux")
lamp.price = 40
print("Tên:",lamp.name)
print("Giá:",lamp.price,"coins")
print("Giảm giá:", lamp.discount,"coins")