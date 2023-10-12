class Book:
    def __init__(self):
        self.title = None
        self.author = None
        self.pageQuantity = None
        self.content = None
        self.typeBook = None

class ScienceBook(Book):
    def __init__(self):
        super().__init__()
        self.literatureList = None
        self.glossary = None

class FictionBook(Book):
    def __init__(self):
        super().__init__()
        self.charactersDict = None

class ManualBook(Book):
    def __init__(self):
        super().__init__()
        self.image = None

class BookBuilder:
    def __init__(self):
        self.book = Book()
    
    def set_baseInfo(self, title, author, pageQuantity, bookType):
        self.book.title = title
        self.book.author = author
        self.book.pageQuantity = pageQuantity
        self.book.bookType = bookType

    def set_scienceBook(self, literatureList, glossary):
        self.book.literatureList = literatureList
        self.book.glossary = glossary

    def set_fictionBook(self, charactersDict):
        self.book.charactersDict = charactersDict

    def set_manualBook(self, image):
        self.book.image = image

    def createPageDict(self):
        self.book.content = {i: None for i in range(1, int(self.book.pageQuantity) + 1)}

    def addContent(self):
        for i in range(1, int(self.book.pageQuantity) + 1):
            self.book.content[i] = input(f'Fill content for page {i}:\n')
     
class Library:
    def __init__(self):
        self.books = {}
        self.tempId = 0
    
    def add_book(self, book_builder):
        self.tempId += 1
        self.books[self.tempId] = book_builder.book
    
    def check_books_shortInfo(self):
        print(f'There are {self.tempId} book(s) in library.')
        for key in self.books:
            book = self.books[key]
            print(f'Book #{key}: {book.title}, Author: {book.author}, Type: {book.bookType}.')

    def readBook(self, bookId, bookPage):
        book = self.books[bookId]
        print(f'PAGE {bookPage}: \n {book.content[bookPage]}')
    
def creatingBook():
    bookType = input('What type of book you want to create? 1. Science. 2. Fiction. 3. Manual \n')
    while True:
        if bookType not in ['1', '2', '3']:
            bookType = input('Error. Use digits 1-3. 1. Science. 2. Fiction. 3. Manual \n')
        else:
            bookType = int(bookType)
            break

    title = input('Enter title of book: ')
    author = input('Enter author of book: ')
    while True:
        try:
            pageQuantity = int(input('Enter quantity of pages: '))
            break
        except:
            pageQuantity = (print('Error. '))

    currentBook = BookBuilder()
    currentBook.set_baseInfo(title, author, pageQuantity, bookTypes[bookType])
    currentBook.createPageDict()
    currentBook.addContent()
    if bookType == 1:
        literatureList = input('Fill literature list: ')
        glossary = input('Fill glossary: ')
        currentBook.set_scienceBook(literatureList, glossary)
    elif bookType == 2:
        characters = input('Add information about charracters: ')
        currentBook.set_fictionBook(characters)
    elif bookType == 3:
        image = input('Enter URL of image: ')
        currentBook.set_manualBook(image)
    library.add_book(currentBook)
    print('Book was succesfully created and added to library')


library = Library()
bookTypes = {1: 'Science', 2: 'Fiction', 3: 'Manual'}

def final():
    while True:
        userDecide = int(input('What do you want to do? 1. Create book. 2. Check library.\n'))
        if userDecide == 1:
            creatingBook()
        elif userDecide == 2:
            library.check_books_shortInfo()
            if len(library.books) == 0:
                continue
            else:
                choiceBook = input('Choose number of book which you want to read or return to menu typing !back: ')
            while True:
                try:
                    choiceBook = int(choiceBook)
                    if choiceBook in library.books:
                        book = library.books[choiceBook]
                        for i in range(1, book.pageQuantity + 1):
                            library.readBook(choiceBook, i)
                            input("Press Enter to continue reading..")
                        
                        print('It was last page.')
                    else:
                        print("Error. This book doesn't exist. Try again")
                    break
                except ValueError:
                    if choiceBook == '!back':
                        final()
                    else:
                        print('Error. Type number.')
                        break
        else:
            print('Error. Use digits 1-2. 1. Create book. 2. Check library.')

final()


