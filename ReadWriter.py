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
        f.close()
    
    def edit_obj(self,target_id,key,value):
        new_data=[]
        with open(self.fp,"rb+") as f:
            while 1:
                try:
                    if pickle.load(f).get_info("ID")==target_id:
                        new_obj=pickle.load(f)
                        new_obj.edit_info(key,value)
                        new_data.append(new_obj)
                    else:
                        new_data.append(pickle.load(f))
                    
                except:
                    break

            f.seek(0)
            f.truncate()
            
            for obj in new_data:
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
