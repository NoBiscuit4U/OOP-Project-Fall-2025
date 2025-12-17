import ReadWriter as rw
import User as usr
import os

class UserManager:
    def __init__(self):
        self.fp_user=os.path.abspath(os.getcwd())+r"\storage\user.dat"
        self.readwrite=rw.ReadWriter(self.fp_user)

    def _get_admins(self):
        admins=[]

        for user in self.readwrite.read_file():
            if user.get_info("creds") == "admin":
                admins.append(user)

        return admins

    def get_users(self):
        return self.readwrite.read_file()

    def get_unique_user(self,key,value):
        return self.readwrite.get_unique_obj(key,value)

    def new_user_write(self,i_id,name,password,creds,email):
        self.readwrite.append_file(usr.User(i_id,name,password,creds,email))
    
    def edit_unique_user(self,id,key,value):
        self.readwrite.edit_obj(id,key,value)

    def remove_unique_user(self,id):
        self.readwrite.remove_obj(id)

    def check_cred(self,name,password):
        for admin in self._get_admins():
            if admin.get_info("name") == name:
                if admin.get_info("password")==password:
                    return True

        return False
    
    def borrow_book(self,user_id,book):
        usr=self.get_unique_user("id",user_id)

        n_books=usr.get_info("books")
        n_books.append(book)
        self.readwrite.edit_obj(user_id,"books",n_books)

    def return_book(self,user_id,book_id):
        usr=self.get_unique_user("id",user_id)
        books=usr.get_info("books")

        for i in range(0,len(books)):
            if books[i].get_info("id")==book_id:
                books.pop(i)
                self.readwrite.edit_obj(user_id,"books",books)
                break

    def get_users_info(self):
        users_info=[]
        for user in self.readwrite.read_file():
            users_info.append(user.get_info_array())
        return users_info

    def get_keys(self):
        return ["ID", "Name", "Password", "Credentials", "Email"]