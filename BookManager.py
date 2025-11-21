import ReadWriter as rw
import Book as bk
import os

class BookManager:
    def __init__(self):
        self.fp_book=os.path.abspath(os.getcwd())+r"\storage/book.dat"
        self.fp_sku=os.path.abspath(os.getcwd())+r"\storage/booksku.dat"
        self.book_readwrite=rw.ReadWriter(self.fp_book)
        self.sku_readwrite = rw.ReadWriter(self.fp_book)

    def get_books(self):
        return self.book_readwrite.read_file()

    def get_unique_book(self,key,value):
        return self.book_readwrite.get_unique_obj(key,value)

    def new_book_write(self,i_id,title,author,pub_date,price):
        self.book_readwrite.append_file(bk.Book(i_id,title,author,pub_date,price))

    def get_keys(self):
        return ["ID","Title","Author","Publish_Date","Price"]