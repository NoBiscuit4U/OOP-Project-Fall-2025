class User:
    def __init__(self,user_id,name,password,creds,email):
        self.user_id=user_id
        self.name=name
        self.password=password
        self.creds=creds
        self.email=email

    def get_info(self,key):
        match key.lower():
            case "id":
                return self.user_id
            case "name":
                return self.name
            case "password":
                return self.password
            case "creds":
                return self.creds
            case "email":
                return self.email
            case _:
                return "INV"

    def edit_info(self,key,value):
        match key.lower():
            case "id":
                self.user_id=value
            case "name":
                self.name=value
            case "password":
                self.password=value
            case "creds":
                self.creds=value
            case "email":
                self.email=value
            case _:
                print("Invalid Key")

    def display_info(self):
        info_contain={"ID":self.user_id,"Name":self.name,"Password":self.password,
                      "Credentials":self.creds,"Email":self.email}

        print("User Info")
        for key in info_contain.keys():
            print(f"    {key}: {info_contain[key]}")
