class Book:
    def __init__(self,i_id,title,author,pub_date,price):
        self.i_id=i_id
        self.title=title
        self.author=author
        self.pub_date=pub_date
        self.price=price

    def get_info(self,key):
        match key.lower():
            case "id":
                return self.i_id
            case "title":
                return self.title
            case "author":
                return self.author
            case "publish date":
                return self.pub_date
            case "price":
                return self.price
            case _:
                return "INV"

    def edit_info(self,key,value):
        match key.lower():
            case "id":
                self.i_id=value
            case "title":
                self.title=value
            case "author":
                self.author=value
            case "publish date":
                self.pub_date=value
            case "price":
                self.price=value
            case _:
                print("Invalid Key")

    def display_info(self):
        info_contain={"ID":self.i_id,"Title":self.title,"Author":self.author,
                      "Publish Date":self.pub_date,"Price":self.price}

        print("Book Info")
        for key in info_contain.keys():
            print(f"    {key}: {info_contain[key]}")
