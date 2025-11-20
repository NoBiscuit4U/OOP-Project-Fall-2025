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

    def check_cred(self,name,password):
        for admin in self._get_admins():
            if admin.get_info("name") == name:
                if admin.get_info("password")==password:
                    return True
            else:
                return False
