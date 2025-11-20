import pickle
import os

class ReadWriter:
    def __init__(self,fp):
        self.fp=fp
        if not os.path.isfile(fp):
            with open(fp, "wb") as f:
                f.close()

    def read_file(self):
        obj_list=[]

        with open(self.fp,"rb") as f:
            while 1:
                 try:
                     obj_list.append(pickle.load(f))
                 except:
                    return obj_list

    def get_unique_obj(self,key,value):
        with open(self.fp,"rb") as f:
            while 1:
                try:
                    if pickle.load(f).get_info(key)==value:
                        return pickle.load(f)
                    elif pickle.load(f).get_info(key)=="INV":
                        print("Invalid Desired Key")
                        return None
                except:
                    return None

    def append_file(self,obj):
        val=self.get_unique_obj("ID",obj.i_id)

        if val == None:
            with open(self.fp, "ab") as f:
                pickle.dump(obj,f)
            f.close()
        else:
            print("Duplicate Object")
