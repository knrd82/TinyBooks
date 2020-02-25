#import Users as usr
import Utils as utils
import tkinter as tk
from tkinter import ttk

i, j = 0, 0
# image = ""
default_bg = "LightSteelBlue1"
default_bg_but = "LightSkyBlue4"
default_fg_but = "snow"
logged_user_type = ""


class LogInWindow:
    form_login = None
    form_passwd = None

    def __init__(self, master):
        #global form_login, form_passwd
        self.master = master
        self.frame1 = tk.Frame(self.master, borderwidth=20, bg=default_bg)
        self.frame2 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        self.frame3 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        self.label = tk.Label(self.master, text="\nWelcome to the Library App", bg=default_bg)
        self.label.pack(fill=tk.BOTH)
        LogInWindow.form_login = create_form_row(self.frame1, "Username: ")
        LogInWindow.form_passwd = create_form_row(self.frame1, "Password: ")
        create_button(self.frame2, "Login", self.check_login, "w", 0, 0)
        create_button(self.frame2, "Quit", self.close_window, "e", 0, 1)
        self.frame1.pack(fill=tk.BOTH)
        self.frame2.pack(fill=tk.Y, side=tk.BOTTOM)
        # self.frame3.pack(fill=tk.Y, side=tk.BOTTOM)

    def check_login(self):
        # TODO: Make this function more pythonic and eliminate D.R.Y.
        login = LogInWindow.form_login.get()
        passwd = LogInWindow.form_passwd.get()
        print("Checking login credentials")
        usr = utils.get_user(login=login)
        if login == usr.login:
            if usr.utype == "admin":
                if passwd == usr.passwd:
                    self.new_admin_window()
                else:
                    print("Wrong admin password provided. Try again")
            elif usr.utype == "user":
                if passwd == usr.passwd:
                    self.new_user_window()
                else:
                    print("Wrong user password provided. Try again")
        else:
            print("User not found")

    def new_admin_window(self):
        global logged_user_type
        zero_the_counters()
        logged_user_type = "admin"
        self.newWindow = tk.Toplevel(self.master)
        self.app = AdminWelcome(self.newWindow)

    def new_user_window(self):
        global logged_user_type
        zero_the_counters()
        logged_user_type = "user"
        self.newWindow = tk.Toplevel(self.master)
        self.app = UserWelcome(self.newWindow)

    def close_window(self):
        self.master.destroy()


class StandardWindow:
    def __init__(self, master):
        self.master = master
        self.title = "Library App"
        self.frame1 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        self.frame2 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        self.label1 = tk.Label(master=self.frame1, text="Welcome, {}".format(logged_user_type), bg=default_bg)
        self.label1.grid(row=0, column=0, padx=10, sticky="w")
        self.button1 = tk.Button(master=self.frame1, text="Log out", command=self.close_windows, bg=default_bg)
        self.button1.grid(row=0, column=1, padx=10, sticky="e")
        self.frame1.pack(fill=tk.X, side=tk.TOP)
        self.frame2.pack(fill=tk.BOTH)

    def close_windows(self):
        print("Closing child window")
        self.master.destroy()

    def new_window(self):
        zero_the_counters()
        self.newWindow = tk.Toplevel(self.master)
        if logged_user_type == "admin":
            self.app = AdminWelcome(self.newWindow)
        elif logged_user_type == "user":
            self.app = UserWelcome(self.newWindow)
        else:
            print("User type not recognized")

# --------------------- ADMIN WINDOWS ----------------------------


class AdminWelcome(StandardWindow):
    def __init__(self, master):
        super().__init__(master)
        create_button(self.frame2, "1. Register new user", self.reg_new_user, ro=0)
        create_button(self.frame2, "2. Check registered users", self.check_reg_users, ro=1)
        create_button(self.frame2, "3. Display rented books", self.display_rent_books, ro=2)
        create_button(self.frame2, "4. Add new book", self.add_book, ro=3)
        create_button(self.frame2, "5. Quit", self.close_windows, ro=4)

    def reg_new_user(self):
        print("Registering new user")
        zero_the_counters()
        self.newWindow = tk.Toplevel(self.master)
        self.app = RegUser(self.newWindow)

    def check_reg_users(self):
        print("Checking registered users")
        self.newWindow = tk.Toplevel(self.master)
        self.app = CheckUsers(self.newWindow)

    def display_rent_books(self):
        print("Displaying rented books")
        self.newWindow = tk.Toplevel(self.master)
        self.app = DisplayRented(self.newWindow)

    def add_book(self):
        print("Adding new book")
        self.newWindow = tk.Toplevel(self.master)
        self.app = AddBook(self.newWindow)


class RegUser(StandardWindow):
    def __init__(self, master):
        super().__init__(master)
        create_form_row(self.frame2, "Name: ")
        create_form_row(self.frame2, "Surname: ")
        create_form_row(self.frame2, "Date of Birth: ")
        create_form_row(self.frame2, "Address Line 1: ")
        create_form_row(self.frame2, "Address Line 2: ")
        create_form_row(self.frame2, "Phone Number: ")
        self.frame3 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        create_button(self.frame3, "Cancel", self.close_windows, "w", 0, 0)
        create_button(self.frame3, "Finish", self.close_windows, "e", 0, 1)
        self.frame3.pack(fill=tk.BOTH, side=tk.BOTTOM)


class CheckUsers(StandardWindow):
    def __init__(self, master):
        super().__init__(master)
        self.frame3 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        create_users_table(self.frame2)
        create_button(self.frame3, "Back", self.close_windows, "e")
        self.frame3.pack(fill=tk.BOTH, side=tk.BOTTOM)


class DisplayRented(StandardWindow):
    def __init__(self, master):
        super().__init__(master)
        self.frame3 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        create_books_table(self.frame2)
        create_button(self.frame3, "Back", self.close_windows, "e")
        self.frame3.pack(fill=tk.BOTH, side=tk.BOTTOM)


class AddBook(StandardWindow):
    def __init__(self, master):
        super().__init__(master)
        self.tit = create_form_row(self.frame2, "Title: ")
        self.aut = create_form_row(self.frame2, "Author: ")
        self.cat = create_form_row(self.frame2, "Category: ")
        self.pag = create_form_row(self.frame2, "Pages: ")
        self.pub = create_form_row(self.frame2, "Publisher: ")
        self.pca = create_form_row(self.frame2, "Price category: ")
        self.frame3 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        create_button(self.frame3, "Submit", self.get_entry_details, "w", 0, 0)
        create_button(self.frame3, "Back", self.close_windows, "e", 0, 1)
        self.frame3.pack(fill=tk.BOTH, side=tk.BOTTOM)

    def get_entry_details(self):
        print("Title: {}\nAuthor: {}\nCategory: {}\nPages: {}\nPublisher: {}\nPrice category: {}\n".format(self.tit.get(), self.aut.get(),
                                                                                                           self.cat.get(), self.pag.get(),
                                                                                                           self.pub.get(), self.pca.get()))


# --------------------- USER WINDOWS ----------------------------


class UserWelcome(StandardWindow):
    def __init__(self, master):
        super().__init__(master)
        create_button(self.frame2, "1. Rent a book", self.rent_book, ro=0)
        create_button(self.frame2, "2. Return a book", self.return_book, ro=1)
        create_button(self.frame2, "3. Check availability", self.check_avail_books, ro=2)
        create_button(self.frame2, "4. Quit", self.close_windows, ro=3)

    def rent_book(self):
        print("Renting book")
        self.newWindow = tk.Toplevel(self.master)
        self.app = RentBook(self.newWindow)

    def return_book(self):
        print("Returning book")
        self.newWindow = tk.Toplevel(self.master)
        self.app = ReturnBook(self.newWindow)

    def check_avail_books(self):
        print("Checking available books")
        self.newWindow = tk.Toplevel(self.master)
        self.app = CheckAvailability(self.newWindow)


class RentBook(StandardWindow):
    def __init__(self, master):
        super().__init__(master)
        self.frame3 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        self.frame4 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        create_books_table(self.frame2)
        self.selection = create_form_row(self.frame3, "Choose a book by ID or Title: ")
        create_button(self.frame4, "Submit", self.get_book_id, "w", 0, 0)
        create_button(self.frame4, "Back", self.close_windows, "e", 0, 1)
        self.frame3.pack(fill=tk.BOTH)
        self.frame4.pack(fill=tk.BOTH, side=tk.BOTTOM)

    def get_book_id(self):
        print("Book id chosen: {}".format(self.selection.get()))


class ReturnBook(RentBook):
    def __init__(self, master):
        super().__init__(master)


class CheckAvailability(StandardWindow):
    def __init__(self, master):
        super().__init__(master)
        self.frame3 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        self.title = create_form_row(self.frame3, "Title: ")
        self.author = create_form_row(self.frame3, "Author: ")
        self.category = create_form_row(self.frame3, "Category: ")
        self.publisher = create_form_row(self.frame3, "Publisher: ")
        self.frame4 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        create_button(self.frame4, "Submit", self.get_entry_details, "w", 0, 0)
        create_button(self.frame4, "Browse", self.browse_books, "e", 0, 1)
        self.frame3.pack(fill=tk.BOTH)
        self.frame4.pack(fill=tk.BOTH, side=tk.BOTTOM)

    def get_entry_details(self):
        print("Title: {}\nAuthor: {}\nCategory: {}\nPublisher: {}".format(self.title.get(), self.author.get(), self.category.get(), self.publisher.get()))

    def browse_books(self):
        print("Displaying available books")
        self.newWindow = tk.Toplevel(self.master)
        self.app = DisplayRented(self.newWindow)


def create_form_row(frame_form, title):
    global i, j
    j = 0
    label = tk.Label(master=frame_form, text=title, bg=default_bg)
    entry = tk.Entry(master=frame_form, width=30)
    label.grid(row=i, column=j, sticky="e")
    j += 1
    entry.grid(row=i, column=j)
    i += 1
    return entry


def create_button(frame, title, comm, stick="", ro=0, col=0):
    button = tk.Button(master=frame, text=title, relief=tk.RAISED, command=comm, width=20, height=1, bg=default_bg_but, fg=default_fg_but)
    button.grid(row=ro, column=col, sticky=stick)


def create_users_table(frame):
    print("Creating users table")
    labels = ("Name", "User type", "Date of Birth", "Address 1", "Address 2")
    tree = ttk.Treeview(frame, columns=labels, selectmode="browse", show='headings')
    for col in labels:
        tree.heading(col, text=col)

    tree.column("Name", minwidth=100, width=100, stretch="NO")
    tree.column("User type", minwidth=100, width=100, stretch="NO")
    tree.column("Date of Birth", minwidth=150, width=150, stretch="NO")
    tree.column("Address 1", minwidth=200, width=200, stretch="NO")
    tree.column("Address 2", minwidth=200, width=200, stretch="NO")

    tree.insert("", "end", "Konrad", values=("Konrad", "Admin", "01/01/1900", "Some address", "City"))
    tree.insert("", "end", "Amy", text="Amy", values=("Amy", "user", "02/02/2002", "Some address", "City"))
    tree.insert("", "end", "test", text="test", values=("test", "user", "03/03/2003", "Some address", "City"))
    tree.grid(row=1, column=0, columnspan=1)


def create_books_table(frame):
    print("Creating books table")
    labels = ("ID", "Title", "Author", "Category", "Pages", "Publisher", "Price cat")
    tree = ttk.Treeview(frame, columns=labels, selectmode="browse", show='headings')
    for col in labels:
        tree.heading(col, text=col)

    tree.column("ID", minwidth=30, width=30, stretch="NO")
    tree.column("Title", minwidth=200, width=200, stretch="NO")
    tree.column("Author", minwidth=150, width=150, stretch="NO")
    tree.column("Category", minwidth=100, width=100, stretch="NO")
    tree.column("Pages", minwidth=50, width=50, stretch="NO")
    tree.column("Publisher", minwidth=100, width=100, stretch="NO")
    tree.column("Price cat", minwidth=70, width=70, stretch="NO")

    tree.insert("", "end", "1", values=("1", "Fundamentals of Wavelets", "Jaideva Goswami", "tech", "228", "Wiley", 1))
    tree.insert("", "end", "2", values=("1", "Fundamentals of Wavelets", "Jaideva Goswami", "tech", "228", "Wiley", 1))
    tree.insert("", "end", "3", values=("1", "Fundamentals of Wavelets", "Jaideva Goswami", "tech", "228", "Wiley", 1))
    tree.grid(row=1, column=0, columnspan=1)


def zero_the_counters():
    global i, j
    i = 0
    j = 0


def main():
    # global image
    root = tk.Tk()
    utils.initialise_library()
    # image = tk.PhotoImage(file="logout-1.gif")
    root.title("Library App")
    app = LogInWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
