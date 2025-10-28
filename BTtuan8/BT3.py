# Lớp cha: Product
class Product:
    def __init__(self, name, original_price, launch_discount=0):
        self.name = name
        self.original_price = original_price
        self.launch_discount = launch_discount

    def price_after_launch_discount(self):
        return max(0, self.original_price - self.launch_discount)
    
    def apply_coupon(self, coupon_code):
        price = self.price_after_launch_discount()
        if coupon_code == "SAVE4":
            price = max(0, price - 4)
        return price


# Giả sử có lớp con Book (để minh họa)
class Book(Product):
    def __init__(self, name, original_price, launch_discount=0, sample_text=""):
        super().__init__(name, original_price, launch_discount)
        self.sample_text = sample_text

    def read_sample(self):
        print(f"Mẫu đọc thử của sách '{self.name}': {self.sample_text}")


# --- Kiểm thử lớp cha ---
t_shirt = Product("Feel good", 30, 4)

print(f"Tên sản phẩm: {t_shirt.name}")
print(f"Giá sau khi giảm ra mắt: {t_shirt.price_after_launch_discount()} xu")
print(f"Giá sau khi áp dụng phiếu giảm giá SAVE4: {t_shirt.apply_coupon('SAVE4')} xu")

# Thử gọi phương thức chỉ dành cho lớp con (Book)
print("\nThử gọi read_sample():")
t_shirt.read_sample()  # <-- Lỗi sẽ xảy ra ở đây!
