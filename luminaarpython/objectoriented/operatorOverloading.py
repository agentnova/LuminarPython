class Book:
    def __init__(self,page):
        self.pages=page
    def __add__(self, other):
        return Book(self.pages+other.pages)
    def __str__(self):
        return str(self.pages)
ob=Book(100)
ob2=Book(200)
ob3=Book(200)



print(ob+ob2+ob3)


# maximum salary print