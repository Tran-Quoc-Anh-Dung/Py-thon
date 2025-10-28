# Lớp cha Vehicle
class Vehicle:
    def __init__(self, model, energy_consumption):
        self.model = model  # tên xe
        self.energy_consumption = energy_consumption  # kWh / 100 km

    def tinh_nang_luong_can_thiet(self, quang_duong):
        """Tính năng lượng cần thiết (kWh) cho quãng đường"""
        return (self.energy_consumption / 100) * quang_duong


# Lớp con ElectricCar kế thừa từ Vehicle
class ElectricCar(Vehicle):
    def __init__(self, model, energy_consumption, battery_capacity):
        super().__init__(model, energy_consumption)
        self.battery_capacity = battery_capacity  # dung lượng pin (kWh)

    def co_the_hoan_thanh_chuyen_di(self, quang_duong):
        """Kiểm tra xem pin có đủ cho chuyến đi không"""
        nang_luong_can = self.tinh_nang_luong_can_thiet(quang_duong)
        print(f"\n🔋 Mẫu xe: {self.model}")
        print(f"   - Mức tiêu thụ năng lượng: {self.energy_consumption} kWh/100km")
        print(f"   - Dung lượng pin: {self.battery_capacity} kWh")
        print(f"   - Năng lượng cần cho {quang_duong} km: {nang_luong_can:.2f} kWh")

        if nang_luong_can <= self.battery_capacity:
            print("✅ Xe có thể hoàn thành chuyến đi!")
            return True
        else:
            print("❌ Pin không đủ cho chuyến đi.")
            return False


# --- Khởi tạo các xe ---
xe1 = ElectricCar("E-Nature", 15, 75)
xe2 = ElectricCar("E-Green", 18, 40)

# --- Tính toán cho chuyến đi 300 km ---
print("=== 🚙 KIỂM TRA KHẢ NĂNG HOÀN THÀNH CHUYẾN ĐI 300 KM ===")

ket_qua1 = xe1.co_the_hoan_thanh_chuyen_di(300)
ket_qua2 = xe2.co_the_hoan_thanh_chuyen_di(300)

# --- Kết luận ---
print("\n=== 🏁 KẾT LUẬN ===")
if ket_qua1 and not ket_qua2:
    print("👉 Bạn nên mua mẫu xe **E-Nature**, vì nó có thể hoàn thành chuyến đi 300 km.")
elif not ket_qua1 and ket_qua2:
    print("👉 Bạn nên mua mẫu xe **E-Green**, vì nó có thể hoàn thành chuyến đi 300 km.")
elif ket_qua1 and ket_qua2:
    print("👉 Cả hai xe đều có thể đi 300 km, bạn có thể chọn theo sở thích khác!")
else:
    print("👉 Không xe nào đủ pin cho chuyến đi 300 km.")
