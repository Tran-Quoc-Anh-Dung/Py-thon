# Định nghĩa lớp Product
class Product:
    def __init__(self, name, original_price, launch_discount):
        self.name = name
        self.original_price = original_price  # giá gốc (xu)
        self.launch_discount = launch_discount  # giảm giá khi ra mắt (xu)
    
    def price_after_launch_discount(self):
        """Giá sau khi áp dụng giảm giá ra mắt"""
        return max(0, self.original_price - self.launch_discount)
    
    def apply_coupon(self, coupon_code):
        """Áp dụng phiếu giảm giá"""
        price = self.price_after_launch_discount()

        # Giả định các phiếu giảm giá có mức giảm cụ thể
        if coupon_code == "SAVE4":
            price = max(0, price - 4)  # giảm 4 xu
        elif coupon_code == "SPRINGSALES30":
            price = round(price * 0.7, 2)  # giảm 30%
        else:
            print("Phiếu giảm giá không hợp lệ!")

        return price
    
    def __str__(self):
        return f"{self.name}: Giá gốc {self.original_price} xu, giảm khi ra mắt {self.launch_discount} xu"

# a. Tạo đối tượng quả bóng bãi biển
giant_ball = Product("Giant ball", 10, 0.5)
print(giant_ball)
print(f"Giá sau giảm ra mắt: {giant_ball.price_after_launch_discount()} xu")
print(f"Giá sau khi áp dụng SAVE4: {giant_ball.apply_coupon('SAVE4')} xu")

print("-" * 50)

# b. Tạo đối tượng cuốn nhật ký
my_adventures = Product("My adventures", 15, 3)
print(my_adventures)
print(f"Giá sau giảm ra mắt: {my_adventures.price_after_launch_discount()} xu")
print(f"Giá sau khi áp dụng SPRINGSALES30: {my_adventures.apply_coupon('SPRINGSALES30')} xu")
