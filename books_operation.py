from os import system 
clear = lambda :system('cls')

from pickle import load
try :
    with open ("books.info","rb") as books_info :
        books = load (books_info)

except(FileNotFoundError):
    books = []

def check_isbn(isbn) :
    for book in books :
        if book['isbn'] == isbn  or len (isbn)!= 6 :
            return True
    return False

def add_book() :
    clear()
    global books   # optional , list of all books
    book = {}
    book['title'] = input ('Enter Title of book :')
    book['author'] = input ('Enter author of book :')
    while True :
        try :
            book['pages'] = int(input('Enter pages of your book :'))
            book['price'] = float (input('Enter price of youe book :'))
            break
        except(ValueError):
            input('all of pages and prices must be number ...pleas try again press any key to try anothor one')
       


    book['isbn'] = input('Enter isbn of your book :')
    if check_isbn (book['isbn'])  :
        input('this book already Exist in database or the number of isbn is not true')
        return False
    books.append(book)
    input ("press any key to back to menu")
    
def list_book():
    clear ()
    for book in books :
        print (f"Title : {book['title']}")
        print (f"Author : {book['author']}")
        print (f"Pages : {book ['pages']}")
        print (f"Price : {book ['price']}")
        print (f"Isbn : {book['isbn']}")
        print ('next book---------------------------')
    input ('press any key to continue')

def find_book():
    clear()
    isbn = input ('Enter Isbn TO Find book :')
    for book in books :
        if book ['isbn'] == isbn :
            print (f"Title : {book['title']}")
            print (f"Author : {book['author']}")
            print (f"Pages : {book ['pages']}")
            print (f"Price : {book ['price']}")
            print (f"Isbn : {book['isbn']}")
            print ('next book---------------------------')   
            break
    else :input ('This book Is Not in books database ,press any key to back in meno')

def delete_book():
    clear ()
    isbn = input ('Enter Isbn TO Find book :')
    for book in books :
        if book['isbn'] == isbn :
            books.remove(book)
            input ('book has been Deleted successfully,press any key')
            break
    else : print(' this book Is Not in database ')

def save_books():
    clear()
    from pickle import dump
    try :
           with open ('books.info','wb') as books_info:
               dump(books,books_info)   # two defult argument   insted of books_info.write(books) but write argument has to be str and books is list so we have to thinking about some package
               print ('books has been saved succsesfully')
    except(PermissionError):
        input ('please chach anothor location for saving')