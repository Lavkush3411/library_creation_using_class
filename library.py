class Library:
    all_books=["h","a","c"]
    l_b=[] #lb=land book ,ab=add book,rb=return book #bn=book name
    d={} #dictionary  of books & landers
    def __init__(self,name):
        self.name=name
#'Displaying book function""
    @classmethod
    def display_book(cls):
        avilable_books=[b for b in (cls.all_books)]
        return avilable_books
# adding boook function
    @classmethod
    def add_book(cls):
        a_b=input('enter book name = ')
        cls.all_books.append(a_b)
#landing book function
    @classmethod
    def land_books(cls):
        lander=input("whats your name = ")
        b_n=input(f"what boook u want to land from {cls.all_books}= ")
        if b_n in cls.all_books:
            cls.l_b.append(b_n)
            cls.all_books.remove(b_n)
            print("books & landers")
            cls.d[b_n]=lander
            print(cls.d)
        else:
            print("book is not in library now choose from below")
# returning book function
    @classmethod
    def return_book(cls):
        r_b=input(f"Which book u want to return from{cls.l_b} = ")
        if r_b in cls.l_b:
            del cls.d[r_b]
            cls.l_b.remove(r_b)
            cls.all_books.append(r_b)
        else:
            print("This book is not on land u can't return")
library_name=Library("\033[1m    Masters Library \033[0m")
print(library_name.name)
print(Library.display_book())
while True:
    try:
        n=int (input("1=display book 2=add book= 3=land book= 4=return a book= 5=quit= ..."))
        if n==1:
            print(Library.display_book())
        if n==2:
            Library.add_book()
        if n==3:
            Library.land_books()
            print(Library.l_b)
        if n==4:
            Library.return_book()
        if n==5:
            break
    except:
        continue