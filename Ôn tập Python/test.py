def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count+=1
    return count
def main():
    text = "Artificial Intelligence"
    result = count_vowels(text)
    print("Danh sách chuỗi là: ", text)
    print("Tổng số phiên âm là: ", result)
main()