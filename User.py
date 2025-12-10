class User:
    def __init__(self,i_id,name,password,creds,email):
        self.i_id=i_id
        self.name=name
        self.password=password
        self.creds=creds
        self.email=email
        self.books_borrowed=[]

    def get_info(self,key):
        match key.lower():
            case "id":
                return self.i_id
            case "name":
                return self.name
            case "password":
                return self.password
            case "creds":
                return self.creds
            case "email":
                return self.email
            case "books":
                return self.books_borrowed
            case _:
                return "INV"

    def edit_info(self,key,value):
        match key.lower():
            case "id":
                self.i_id=value
            case "name":
                self.name=value
            case "password":
                self.password=value
            case "creds":
                self.creds=value
            case "email":
                self.email = value
            case "books":
                self.books=value
            case _:
                print("Invalid Key")

    def borrow_book(self,book):
        self.books_borrowed.append(book)

    def return_book(self,id):
        for i in range(0,len(self.books_borrowed)):
            if self.books_borrowed[i].get_info("id")==id:
                self.books_borrowed.pop(i)
                break


    def display_info(self):
        info_contain={"ID":self.i_id,"Name":self.name,"Password":self.password,
                      "Credentials":self.creds,"Email":self.email}

        print("User Info")
        for key in info_contain.keys():
            print(f"    {key}: {info_contain[key]}")

    def get_info_array(self):
        return[self.i_id,self.name,self.password,self.creds,self.email]