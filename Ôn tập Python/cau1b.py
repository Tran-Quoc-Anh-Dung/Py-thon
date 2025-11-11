def count_vowels(s):
    """Đếm số nguyên âm trong chuỗi s."""
    vowels = "aeiouAEIOU"  # liệt kê tất cả nguyên âm (cả chữ thường và hoa)
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


def main():
    text = "Artificial Intelligence"
    result = count_vowels(text)
    print(f"Chuỗi: {text}")
    print(f"Số nguyên âm: {result}")

main()
