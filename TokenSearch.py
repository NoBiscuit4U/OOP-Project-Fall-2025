class TokenSearch:
    def __init__(self,book_manager):
        self.book_manager=book_manager

    def token_search(self,string,key,seperator=""):
        string=string.lower()
        return_arr=[]

        if seperator!="":
            s_tokens = string.split(seperator)
        else:
            s_tokens = [string]

        for book in self.book_manager.get_books():
            key_v=str(book.get_info(key)).lower()

            if seperator in key_v:
                b_tokens=key_v.split(seperator)
            else:
                b_tokens=[key_v]

            for s_token in s_tokens:
                for b_token in b_tokens:
                    if s_token==b_token:
                        return_arr.append(book.get_info_array())

        return return_arr