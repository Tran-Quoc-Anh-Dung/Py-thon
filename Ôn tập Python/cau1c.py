def average(numbers):
    """Trả về giá trị trung bình của danh sách numbers."""
    if len(numbers) == 0:  # tránh chia cho 0
        return 0
    total = sum(numbers) / len(numbers)  # tính tổng các phần tử
    return total
def main():
    nums = [4, 7, 2, 9, 5]
    avg = average(nums)
    print(f"Danh sách: {nums}")
    print(f"Giá trị trung bình: {avg}")

main()
