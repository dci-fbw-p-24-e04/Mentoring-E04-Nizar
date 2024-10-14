my_string = "Hello"
new_string = my_string + ' Wrold!'
my_int = 7
new_int = my_int + 8
# print(dir(new_string))
# print('-'*50)
# print(dir(new_int))

class Book:
    def __init__(self,title,author,num_of_pages):
        self.title  = title 
        self.author = author
        self.num_of_pages = num_of_pages
        
    def __str__(self):# we make our object printable
        return f"{self.title} by {self.author}"
    
    def __repr__(self) :
        return f"Book({self.title}, {self.author}, {self.num_of_pages})"
        
    def __len__(self):
        return self.num_of_pages
    
    def __add__(self,pages):
        if isinstance(pages,int):
            self.num_of_pages += pages
            return Book(self.title,self.author,self.num_of_pages)
        elif isinstance(pages,Book):
            total = self.num_of_pages + pages.num_of_pages
            return Book('Combined book','Various authors',total)
        
    def __eq__(self, other_book) :#==
        return self.num_of_pages == other_book.num_of_pages
    
    def __lt__(self,pages):
        if isinstance(pages,int):
            return self.num_of_pages < pages
        elif isinstance(pages,Book):
            return self.num_of_pages < pages.num_of_pages
        
    def __gt__(self,pages):
        if isinstance(pages,int):
            return self.num_of_pages > pages
        elif isinstance(pages,Book):
            return self.num_of_pages > pages.num_of_pages

    #we can also make our object behave like a dict
    def __getitem__(self,key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_of_pages':
            return self.num_of_pages
        else:
            return 'Invalid keyword for the book object'
        
    def __setitem__(self,key,value):
        if key == 'title':
            self.title = value
        elif key == 'author':
            self.author = value
        elif key == 'num_of_pages':
            self.num_of_pages = value
        else:
            return 'Invalid keyword for the book object'
book_1 = Book("To Kill a Mockingbird", "Harper Lee", 320)
book_2 = Book("To Kill a Mockingbird Part 2", "Harper Lee", 220)
print(id(book_1))
print(book_1)
print(repr(book_1))
print(len(book_1))
book_3 = book_1 + book_2
print(book_3)
print(book_3.num_of_pages)
updated_book = book_1 + 100
print(updated_book)
print(updated_book.num_of_pages)
print('equal?',book_1==book_2)
print(book_1 < 400)
print(book_2 < book_1)
print(book_1 > 400)
print(book_2 > book_1)
print(book_1['title'])
print(book_2['author'])
print(book_1['price'])
book_2['author'] = 'some guy that i forgot the name'#setting a new value
print(book_2['author'])