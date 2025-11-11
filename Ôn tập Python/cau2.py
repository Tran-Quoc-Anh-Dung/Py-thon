# lớp Book
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        """In thông tin sách."""
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Price: {self.price}")


# lớp Library
class Library:
    def __init__(self):
        self.books = []  # danh sách các đối tượng Book

    def add_book(self, book):
        """Thêm sách vào thư viện."""
        self.books.append(book)

    def search_by_author(self, author_name):
        """Trả về danh sách các sách của tác giả author_name."""
        return [book for book in self.books if book.author == author_name]

    def get_total_value(self):
        """Tính tổng giá trị tất cả sách trong thư viện."""
        return sum(book.price for book in self.books)


# chương trình chính
def main():
    # tạo đối tượng Book
    book1 = Book(1, "Cho tôi xin một vé đi tuổi thơ", "Nguyễn Nhật Ánh", 50000)
    book2 = Book(2, "Tuổi thơ dữ dội", "Phùng Quán", 60000)
    book3 = Book(3, "Cô gái đến từ hôm qua", "Nguyễn Nhật Ánh", 55000)

    # tạo đối tượng Library
    my_library = Library()

    # thêm sách vào thư viện
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # in toàn bộ thông tin sách
    print("=== Danh sách tất cả sách ===")
    for book in my_library.books:
        book.display_info()

    # tìm sách của tác giả "Nguyễn Nhật Ánh"
    print("\n=== Sách của tác giả 'Nguyễn Nhật Ánh' ===")
    books_by_author = my_library.search_by_author("Nguyễn Nhật Ánh")
    for book in books_by_author:
        book.display_info()

    # in tổng giá trị các sách
    total_value = my_library.get_total_value()
    print(f"\nTổng giá trị các sách trong thư viện: {total_value} VND")

main()
