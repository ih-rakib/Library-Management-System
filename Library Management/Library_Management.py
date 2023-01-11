class User : 
    def __init__(self,name,roll,password) -> None:
        self.name = name
        self.roll = roll
        self.password = password
        self.borrowed_books = []
        self.returned_books = []

class Library : 
    def __init__(self,book_list) -> None:
        self.book_list = book_list
    
    def borrow_book(self,bookName,user) : 
        for book in self.book_list :
            if book == bookName : 
                if bookName in  user.borrowed_books : 
                    print('You have already taken this book') 
                    return
                if self.book_list[book] == 0 :
                    print('All of this book have already taken') 
                    return
                self.book_list[book] -= 1
                user.borrowed_books.append(bookName)
                print('Successfully Borrowed') 
                return
            
        print('Book is not available') 
    
    def return_book(self,bookName,user) :
        for book in self.book_list : 
            if book == bookName : 
               if book in currentUser.borrowed_books : 
                 self.book_list[book] += 1
                 user.borrowed_books.remove(bookName) 
                 user.returned_books.append(bookName)
                 print('Book returned successfully')
                 return
            else : 
                print('You have not even borrowed this book according to our records!')
                return
                
        print('This book is not of our library') 
        return
    
    def check_availability(self) :
        for book in self.book_list : 
            if self.book_list[book] > 0 : 
                print(f'{book} : {self.book_list[book]}')
                return 
    
    def donate_books(self,bookName,amount) : 
        for book in self.book_list : 
            if book == bookName : 
                self.book_list[book] += amount
                print('Thanks for donating') 
                return
                
        self.book_list[bookName] = amount
        print('Thanks for donating') 

library = Library({'English' : 2, 'Bangla' : 4, 'Mathematics' : 3, 'Physics' : 2})
allUser = []
currentUser = None

while True : 
    if currentUser == None : 
        print('Not logged in\nPlease login or create account(L/C)')
        option = input()
        if option == 'L' : 
            roll = int(input('Roll : '))
            password = input('Password : ') 
            match = False
            for user in allUser : 
                if user.roll == roll and user.password == password : 
                    currentUser = user
                    match = True
            if match == False : 
                print('No user found') 
        else : 
            name = input('Name : ') 
            roll = int(input('Roll : '))
            password = input('Password : ')
            user = User(name,roll,password)
            currentUser = user
            allUser.append(user)
    else : 
        print('Options : ')
        print('----------\n') 
        print('1. Borrow a book') 
        print('2. Return Book')
        print('3. Borrowed Books')
        print('4. Returned Books')
        print('5. Check Avaibility')
        print('6. Donate Books')
        print('7. Logout\n')
        choice = int(input('Enter your choice : '))
        if choice == 1 : 
            bookName = input('Book Name : ')
            library.borrow_book(bookName,currentUser)
        elif choice == 2 : 
            bookName = input('Book Name : ')
            library.return_book(bookName,currentUser)
        elif choice == 3 : 
            print(currentUser.borrowed_books)
        elif choice == 4 : 
            print(currentUser.returned_books)
        elif choice == 5 : 
            library.check_availability()
        elif choice == 6 : 
            bookName = input('Book Name : ') 
            amount = int(input('Amount : ')) 
            library.donate_books(bookName,amount)
        elif choice == 7 :
            currentUser = None
        
        print('\n\n') 
