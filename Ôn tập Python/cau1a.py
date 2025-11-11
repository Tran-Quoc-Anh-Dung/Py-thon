def is_prime(n):
    """Kiểm tra xem n có phải là số nguyên tố hay không."""
    if n < 2:  # 0,1 không phải là số nguyên tố
        return False
    for i in range(2, int(n**0.5) + 1):  # chỉ cần kiểm tra đến căn bậc hai của n
        if n % i == 0:
            return False
    return True


def main():
    primes = [n for n in range(1, 51) if is_prime(n)]
    print("Các số nguyên tố từ 1 đến 50 là:")
    print(primes)


main()