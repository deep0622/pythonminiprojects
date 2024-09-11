class library:
    def __init__(self):
        self.nobooks = 0
        self.books = []

    def addbook(self,book):
        self.books.append(book)
        self.nobooks = len(self.books)

    def showinfo(self):
        print(f"the has {self.nobooks} books in the library. the books are ")
        for i in self.books:
            print(i)

l1 = library()
l1.addbook("python")
l1.addbook("java")
l1.addbook("js")
l1.showinfo()
