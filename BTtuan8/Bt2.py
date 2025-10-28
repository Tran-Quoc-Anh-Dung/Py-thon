# Định nghĩa lớp Product
class Product:
    def __init__(self, name, original_price, launch_discount=0):
        self.name = name
        self.original_price = original_price  # giá gốc (xu)
        self.launch_discount = launch_discount  # giảm giá khi ra mắt (xu)
    
    def price_after_launch_discount(self):
        """Tính giá sau khi áp dụng giảm giá ra mắt"""
        return max(0, self.original_price - self.launch_discount)
    
    def apply_coupon(self, coupon_code):
        """Áp dụng phiếu giảm giá cho sản phẩm"""
        price = self.price_after_launch_discount()

        # Các loại phiếu giảm giá giả định
        if coupon_code == "SUMMER10":
            price = round(price * 0.9, 2)  # giảm 10%
        elif coupon_code == "SAVE4":
            price = max(0, price - 4)  # giảm 4 xu
        elif coupon_code == "SPRINGSALES30":
            price = round(price * 0.7, 2)  # giảm 30%
        else:
            print(f"Phiếu giảm giá '{coupon_code}' không hợp lệ.")
        return price

    def __str__(self):
        return f"{self.name}: Giá gốc {self.original_price} xu, giảm khi ra mắt {self.launch_discount} xu"


# --- Khởi tạo các sản phẩm ---
lux = Product("Lux", 40, 0)
giant_ball = Product("Giant ball", 10, 0.5)
my_adventures = Product("My adventures", 15, 3)

# --- Hiển thị thông tin từng sản phẩm ---
products = [
    (lux, "SUMMER10"),
    (giant_ball, "SAVE4"),
    (my_adventures, "SPRINGSALES30")
]

print("=== CỬA HÀNG TRỰC TUYẾN ===\n")

for product, coupon in products:
    print(product)
    print(f"Giá sau giảm ra mắt: {product.price_after_launch_discount()} xu")
    print(f"Giá sau khi áp dụng phiếu giảm giá {coupon}: {product.apply_coupon(coupon)} xu")
    print("-" * 50)
