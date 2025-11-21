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
                    if pickle.load(f).get_info(key,value)==value:
                        return pickle.load(f)
                except:
                    return None
        f.close()
    
    def edit_obj(self,target_id,key,value):
        data=self.read_file()
        with open(self.fp,"wb") as f:   
            for obj in data:
                if int(obj.get_info("ID"))==int(target_id):
                    n_obj=obj
                    n_obj.edit_info(key,value)
                    print(n_obj.get_info("Title"))
                    print("TARGET DUMP")
                    pickle.dump(n_obj,f)
                else:
                    pickle.dump(obj,f)

        f.close()
    
    def remove_obj(self,target_id):
        data=self.read_file()
        with open(self.fp,"wb") as f:   
            for obj in data:
                if not int(obj.get_info("ID"))==int(target_id):
                    pickle.dump(obj,f)

        f.close()

    def append_file(self,obj):
        val=self.get_unique_obj("ID",obj.i_id)

        if val == None:
            with open(self.fp, "ab") as f:
                pickle.dump(obj,f)
            f.close()
        else:
            print("Duplicate Object")
