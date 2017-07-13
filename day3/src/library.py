from collections import defaultdict


class Library(object):
    """
    A Library class.

    """

    def __init__(self, books=None):
        """
        INPUT:
            - books: iterable of strs (optional)
        Initialize a library with the given books. If no books given,
        initialize with no books. All books start checked in.
        """
        self.users = defaultdict(set)
        if books:
            self.books = {book: None for book in books}
        else:
            self.books = dict()

    def checkout(self, book, name):
        """
        INPUT:
            - book: str
            - name: str
        Given a book and a person's name, checkout the book and return True.
        If it's not possible to checkout, do nothing and return False.
        """
        if book not in self.books or self.books[book]:
            # cannot checkout book
            return False
        self.books[book] = name
        return True

    def checkin(self, book):
        '''
        INPUT:
            - book: str
        Given a book, return the book and return True.
        If it's not possible to return the book, do nothing and return False.
        '''
        if book not in self.books or not self.books[book]:
            # not a book or already checked in
            return False
        self.books[book] = None
        return True

    def book_holder(self, book):
        '''
        INPUT:
            - book: str
        Given a book, return who has the book. Return None if nobody has the
        book.
        '''
        return self.books.get(book, None)

    def add_book(self, book):
        '''
        INPUT:
            - book: str
        Add the given book to the library and return True.
        If the book is already owned by the library, do nothing and return
        False.
        '''
        if book in self.books:
            # already have book
            return False
        self.books[book] = None
        return True

    def is_checkedin(self, book):
        '''
        INPUT:
            - book: str
        Return True iff the book is in the library.
        '''
        return book in self.books and not self.books[book]

    # TODO: Add book_checkedout method
    def books_checkedout(self, name):
        """
        INPUT:
            - name: str
        Return the list of books checked out by the given person.

        To make this efficient, in the __init__ method,
        create another instance variable called users which has every user and a set of the books they have checked out.
        This means every time you check a book in or out you will need to update both dictionaries.
        You might want to use a defaultdict instead of a standard dict.
        """
        return set(self.books)

    def all_books(self):
        '''
        Return a list of all the books the library owns.
        '''
        return sorted(self.books)

    def all_checkedin_books(self):
        '''
        Return a list of all the books that are currently checked in to the
        library.
        '''
        return sorted(book for book in self.books if self.is_checkedin(book))

    def __len__(self):
        '''
        Return the number of books owned by the library.
        '''
        return len(self.all_books())
