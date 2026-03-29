class Library:
    def __init__(self):
        self.books = {}
        self.borrowed = {}

    def add_book(self, title, copies):
        if title in self.books:
            self.books[title] += copies
        else:
            self.books[title] = copies

    def borrow_book(self, user, title):
        if title in self.books and self.books[title] > 0:
            self.books[title] -= 1
            if user not in self.borrowed:
                self.borrowed[user] = []
            self.borrowed[user].append(title)
            return True
        return False

    def return_book(self, user, title):
        if user in self.borrowed and title in self.borrowed[user]:
            self.books[title] += 1
            return True
        return False

    def total_books(self):
        total = 0
        for t in self.books:
            total += len(t)
        return total

    def available_books(self):
        return len(self.books)

    def user_books_count(self, user):
        if user in self.borrowed:
            return len(set(self.borrowed[user]))
        return 0

    def most_popular_book(self):
        count = {}
        for user in self.borrowed:
            for book in self.borrowed[user]:
                count[book] = count.get(book, 0) + 1
        if count:
            return min(count, key=count.get)
        return None


class LibrarySystem:
    def __init__(self):
        self.lib = Library()

    def setup(self):
        self.lib.add_book("Math", 5)
        self.lib.add_book("Physics", 3)
        self.lib.add_book("CS", 4)

    def simulate(self):
        users = ["Ali", "Sara", "Ahmed"]
        actions = [
            ("borrow", "Math"),
            ("borrow", "Physics"),
            ("return", "Math"),
            ("borrow", "CS"),
        ]

        for user in users:
            for action, book in actions:
                if action == "borrow":
                    self.lib.borrow_book(user, book)
                else:
                    self.lib.return_book(user, book)

    def report(self):
        print("Total Books:", self.lib.total_books())
        print("Available Titles:", self.lib.available_books())
        for user in ["Ali", "Sara", "Ahmed"]:
            print(user, "has", self.lib.user_books_count(user), "books")
        print("Most Popular:", self.lib.most_popular_book())


system = LibrarySystem()
system.setup()
system.simulate()
system.report()
