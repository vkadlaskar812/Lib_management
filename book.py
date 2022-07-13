class Book:
    def __init__(self,id,name,description,isbn,page_cnt,issued,author,year ):

        self.id = id
        self.name = name
        self.description = description
        self.isbn = isbn
        self.page_cnt = page_cnt
        self.issued = issued
        self.author = author
        self.year = year

    def to_dict(self):
        dictionary={
            "id" : self.id,
            "name" : self.name,
            "description" : self.description,
            "isbn" : self.isbn,
            "page_count" : self.page_cnt,
            "issued" : self.issued,
            "author" : self.author,
            "year" : self.year
        }
        return dictionary