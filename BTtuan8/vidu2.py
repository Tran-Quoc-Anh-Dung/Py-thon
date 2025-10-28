class Product1:

    """Lớp đại diện cho một sản phẩm"""

    #

    #--- hàm khởi tạo

    def __init__(self, name):

        #khởi tạo
        self.name=name
        self.price = 0
        self.discount = 0

    #----- phương pháp

    def apply_coupon(self, coupon):

        """Cap nhat discount dựa trên coupon"""

        if coupon == "SAVE4":
            self.discount+= 4
            print("Coupon SAVE4 ĐƯỢC ÁP DỤNG")
        elif coupon=="SUMMER10":
            self.discount+= 10
            print("Coupon SAVE4 ĐƯỢC ÁP DỤNG")

        else:
            print("Coupon của bạn KHÔNG ĐƯỢC ÁP DỤNG")

    def calculate_price(self):

        """Tính số tiền phải trả"""
        updated_price=self.price-self.discount
        return updated_price

    ## PHƯƠNG PHÁP TÍCH HỢP

    def __str__(self):
        """In các thuộc tính ra"""
        return "Tên: " + self.name
    
#thiết lập sản phẩm với thuộc tính của nó
t_shirt = Product1("Feel good")
t_shirt.price = 30
t_shirt.discount = 4
print("Tên:",t_shirt.name,"! Giá ban đầu:", t_shirt.price,"coins! Giá khuyến mãi:",t_shirt.discount,"coins.")

#tính toán giá sau khi áp dụng mã giảm giá
print("-> Giá sau khi áp dụng giảm giá")
t_shirt_price = t_shirt.calculate_price()
print("Giá:",t_shirt_price,"coins.")

#áp dụng coupon
print("Áp dụng coupon")
t_shirt.apply_coupon("SAVE4")
print("Khuyến mãi:",t_shirt.discount,"coins.")

#tính toán giá sau cùng sau khi giảm giá và discount
print("->Giá sau khi áp dụng giảm giá và coupon")
t_shirt_price = t_shirt.calculate_price()
print("Giá:",t_shirt_price,"coins.")