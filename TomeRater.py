class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "User email address has been changed to " + address

    def __repr__(self):
        representation = "Username: " + self.name + ". Email Address: " + self.email + ". Books Read: " + str(len(list(self.books.keys())))
        return representation

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        avg = 0
        for rating in self.books.values():
            avg += rating
        return avg / len(self.books.values())

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "ISBN has been changed to: " + str(new_isbn)

    def add_rating(self, rating):
        if rating and 0 <= rating <= 4:
            self.ratings.append(rating)
        elif rating == None:
            None
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_average_rating(self):
        avg = 0
        for rating in self.ratings:
            avg += rating
        return avg / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return self.title

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author = self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} book on {subject}".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "Object containing both users and books"

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        for book in self.books:
            if new_book.isbn == book.isbn:
                raise Exception("Book with isbn:{isbn} already exists!".format(isbn=isbn))
        return new_book

    def create_novel(self, title, author, isbn):
        new_fiction = Fiction(title, author, isbn)
        return new_fiction

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
            user = self.users.get(email, None)
            user.read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {}".format(email))

    def add_user(self, name, email, user_books = None):
        valid_email_endings = [".com", ".org", ".edu"]
        count = 0
        for ending in valid_email_endings:
            if ending in email:
                count += 1
        if count != 1:
            print("Email:{email} is not a valid email address!".format(email = email))
        else:
            if "@" not in email:
                print("Email:{email} is not a valid email address!".format(email = email))
            elif email in self.users:
                print("User with email:{email} already exists!".format(email = email))
            else:
                new_user = User(name,email)
                self.users[email] = new_user
                if user_books is not None:
                    for book in user_books:
                        self.add_book_to_user(book, email)

    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for user in self.users.keys():
            print(user)

    def most_read_book(self):
        most_read = None
        count = 0
        for book in self.books.keys():
            if self.books[book] > count:
                count = self.books[book]
            if self.books[book] == count:
                most_read = book
        return most_read

    def highest_rated_book(self):
        best_book = None
        highest_rating = 0
        for book in self.books.keys():
            if User.get_average_rating(self) > highest_rating:
                highest_rating = User.get_average_rating(self)
                best_book = book
        return best_book

    def most_positive_user(self):
        highest_rating = 0
        best_user = None
        for user in self.users.values():
            average = User.get_average_rating(self)
            if User.get_average_rating(self) > highest_rating:
                highest_rating = User.get_average_rating(self)
                best_user = user
        return best_user
