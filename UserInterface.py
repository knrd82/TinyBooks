import Utils as utils
import Users as usrs
import Book as bk
import tkinter as tk
import datetime
from tkinter import ttk

i, j = 0, 0
# image = ""
default_bg = "LightSteelBlue1"
default_bg_but = "LightSkyBlue4"
default_fg_but = "snow"
logged_user_type = ""
logged_user_id = ""
user_types = [("Admin", "1"), ("User", "2")]
today_date = datetime.datetime.today()


class LogInWindow:
    form_login = None
    form_passwd = None

    def __init__(self, master):
        self.master = master
        self.frame1 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        self.frame2 = tk.Frame(self.master, borderwidth=0, bg=default_bg)
        self.frame3 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        self.label = tk.Label(self.master, text="\nWelcome to the Library App", bg=default_bg)
        self.label.pack(fill=tk.BOTH)
        LogInWindow.form_login = create_form_row(self.frame1, "Username: ")
        LogInWindow.form_passwd = create_form_row(self.frame1, "Password: ")
        create_button(self.frame3, "Login", self.check_login, "w", 0, 0)
        create_button(self.frame3, "Quit", self.close_window, "e", 0, 1)
        self.lab = tk.Label(self.frame2, bg=default_bg, fg="red", font=("Helvetica", 10))
        self.lab.pack(fill=tk.BOTH)
        self.frame1.pack(fill=tk.BOTH)
        self.frame2.pack(fill=tk.X)
        self.frame3.pack(fill=tk.Y, side=tk.BOTTOM)

    def check_login(self):
        global logged_user_id
        global logged_user_type
        show_message(self.lab, "")
        login = LogInWindow.form_login.get()
        passwd = LogInWindow.form_passwd.get()
        usr = utils.get_user(login=login)
        if login == "" or passwd == "":
            show_message(self.lab, "You need to provide login and password")
        else:
            if usr:
                if login == usr.login:
                    if passwd == usr.passwd:
                        clear_input(LogInWindow.form_login)
                        clear_input(LogInWindow.form_passwd)
                        logged_user_id = usr.uid
                        logged_user_type = usr.utype
                        if logged_user_type == "admin":
                            self.new_admin_window()
                        else:
                            self.new_user_window()
                    else:
                        show_message(self.lab, "Wrong password provided. Try again")
            else:
                show_message(self.lab, "User not found")

    def new_admin_window(self):
        zero_the_counters()
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.resizable(False, False)
        self.app = AdminWelcome(self.newWindow)

    def new_user_window(self):
        zero_the_counters()
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.resizable(False, False)
        self.app = UserWelcome(self.newWindow)

    def close_window(self):
        self.master.destroy()
        utils.close_library()


class StandardWindow:
    def __init__(self, master):
        self.master = master
        self.title = "Library App"
        self.frame1 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        self.frame2 = tk.Frame(self.master, borderwidth=5, bg=default_bg)
        self.label1 = tk.Label(master=self.frame1, text="Welcome, {}".format(logged_user_type), bg=default_bg)
        self.label1.grid(row=0, column=0, padx=10, sticky="w")
        self.button1 = tk.Button(master=self.frame1, text="Log out", command=self.close_windows, bg=default_bg)
        self.button1.grid(row=0, column=1, padx=10, sticky="e")
        self.frame1.pack(fill=tk.X, side=tk.TOP)
        self.frame2.pack(fill=tk.BOTH)

    def close_windows(self):
        self.master.destroy()

# --------------------- ADMIN WINDOWS ----------------------------


class AdminWelcome(StandardWindow):
    def __init__(self, master):
        super().__init__(master)
        create_button(self.frame2, "1. Register new user", self.reg_new_user, ro=0)
        create_button(self.frame2, "2. Edit users", self.edit_user, ro=1)
        create_button(self.frame2, "3. Check registered users", self.check_reg_users, ro=2)
        create_button(self.frame2, "4. Display rented books", self.display_rent_books, ro=3)
        create_button(self.frame2, "5. Add new book", self.add_book, ro=4)
        create_button(self.frame2, "6. Quit", self.close_windows, ro=5)

    def reg_new_user(self):
        print("Registering new user")
        zero_the_counters()
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.resizable(False, False)
        self.app = RegUser(self.newWindow)

    def edit_user(self):
        print("Editing user")
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.resizable(False, False)
        self.app = EditUser(self.newWindow)

    def check_reg_users(self):
        print("Checking registered users")
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.resizable(False, False)
        self.app = CheckUsers(self.newWindow)

    def display_rent_books(self):
        print("Displaying rented books")
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.resizable(False, False)
        self.app = DisplayRented(self.newWindow)

    def add_book(self):
        print("Adding new book")
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.resizable(False, False)
        self.app = AddBook(self.newWindow)


class RegUser(StandardWindow):
    form_login = None
    form_passwd = None
    form_fullname = None
    form_dob = None
    form_addr1 = None
    form_addr2 = None
    form_phone = None
    v = None

    def __init__(self, master):
        super().__init__(master)
        global i, j
        self.frame3 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        self.frame4 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        RegUser.v = tk.StringVar()
        RegUser.f = tk.StringVar()
        RegUser.v.set("1")
        RegUser.f.set("")
        self.label2 = tk.Label(master=self.frame2, borderwidth=0, bg=default_bg)
        self.label2.grid(columnspan=2, row=0)
        for text, mode in user_types:
            b = tk.Radiobutton(self.frame2, bg=default_bg, text=text, variable=RegUser.v, value=mode)
            b.grid(row=1, column=j)
            j += 1
        RegUser.form_login = create_form_row(self.frame3, "* Username: ")
        RegUser.form_passwd = create_form_row(self.frame3, "* Password: ")
        RegUser.form_fullname = create_form_row(self.frame3, "* Full Name: ")
        RegUser.form_dob = create_form_row(self.frame3, "Date of Birth: ")
        RegUser.form_addr1 = create_form_row(self.frame3, "Address Line 1: ")
        RegUser.form_addr2 = create_form_row(self.frame3, "Address Line 2: ")
        RegUser.form_phone = create_form_row(self.frame3, "Phone Number: ")
        create_button(self.frame4, "Cancel", self.close_windows, "w", 0, 0)
        create_button(self.frame4, "Finish", self.save_user, "e", 0, 1)
        self.frame3.pack(fill=tk.BOTH)
        self.frame4.pack(fill=tk.BOTH, side=tk.BOTTOM)

    def save_user(self):
        print("Saving user to file...")
        utype = user_types[int(RegUser.v.get())-1][0]
        utils.add_user(utype, RegUser.form_fullname.get(), RegUser.form_login.get(), RegUser.form_passwd.get(), 0.0,
                       RegUser.form_dob.get(), RegUser.form_addr1.get(), RegUser.form_addr2.get(),
                       RegUser.form_phone.get(), today_date.strftime('%d/%m/%Y'))
        self.close_windows()

    def close_windows(self):
        super(RegUser, self).close_windows()


class EditUser(StandardWindow):
    form_userId = None
    form_login = None
    form_fullname = None
    form_dob = None
    form_addr1 = None
    form_addr2 = None
    form_phone = None
    text_login = None
    text_fullname = None
    text_dob = None
    text_addr1 = None
    text_addr2 = None
    text_phone = None

    def __init__(self, master):
        super().__init__(master)
        global i, j
        self.frame3 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        self.frame4 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        self.label2 = tk.Label(master=self.frame2, borderwidth=5, bg=default_bg, fg="red", font=("Helvetica", 10))
        self.label2.grid(columnspan=2, row=0)

        EditUser.text_login = tk.StringVar()
        EditUser.text_fullname = tk.StringVar()
        EditUser.text_dob = tk.StringVar()
        EditUser.text_addr1 = tk.StringVar()
        EditUser.text_addr2 = tk.StringVar()
        EditUser.text_phone = tk.StringVar()

        EditUser.form_userId = create_form_row(self.frame3, "User ID: ")
        EditUser.form_login = create_form_row(self.frame3, "* Username: ", EditUser.text_login)
        EditUser.form_fullname = create_form_row(self.frame3, "* Full Name: ", EditUser.text_fullname)
        EditUser.form_dob = create_form_row(self.frame3, "Date of Birth: ", EditUser.text_dob)
        EditUser.form_addr1 = create_form_row(self.frame3, "Address Line 1: ", EditUser.text_addr1)
        EditUser.form_addr2 = create_form_row(self.frame3, "Address Line 2: ", EditUser.text_addr2)
        EditUser.form_phone = create_form_row(self.frame3, "Phone Number: ", EditUser.text_phone)
        create_button(self.frame4, "Find", self.display_user, "w", 0, 0)
        create_button(self.frame4, "Save", self.save_user, "e", 0, 1)
        self.frame3.pack(fill=tk.BOTH)
        self.frame4.pack(fill=tk.BOTH, side=tk.BOTTOM)

    def display_user(self):
        show_message(self.label2, "")
        temp_id = int(EditUser.form_userId.get())
        temp_user = utils.get_user(uid=temp_id)
        if temp_user:
            print(temp_user)
            EditUser.text_login.set(temp_user.login)
            EditUser.text_fullname.set(temp_user.name)
            EditUser.text_dob.set(temp_user.dob)
            EditUser.text_addr1.set(temp_user.addr1)
            EditUser.text_addr2.set(temp_user.addr2)
            EditUser.text_phone.set(temp_user.phone)
        else:
            show_message(self.label2, "User not found. Please try again")
            EditUser.text_login.set("")
            EditUser.text_fullname.set("")
            EditUser.text_dob.set("")
            EditUser.text_addr1.set("")
            EditUser.text_addr2.set("")
            EditUser.text_phone.set("")


    def save_user(self):
        print("Saving user to file...")
        #utype = user_types[int(RegUser.v.get()) - 1][0]
        #utils.add_user(utype, RegUser.form_fullname.get(), RegUser.form_login.get(), RegUser.form_passwd.get(), 0.0,
        #               RegUser.form_dob.get(), RegUser.form_addr1.get(), RegUser.form_addr2.get(),
        #               RegUser.form_phone.get(), today_date.strftime('%d/%m/%Y'))
        self.close_windows()

    def close_windows(self):
        super(EditUser, self).close_windows()


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
        create_button(self.frame3, "Submit", self.save_book, "w", 0, 0)
        create_button(self.frame3, "Back", self.close_windows, "e", 0, 1)
        self.frame3.pack(fill=tk.BOTH, side=tk.BOTTOM)

    def save_book(self):
        print("Saving new book to file...")
        utils.add_book(self.tit.get(), self.aut.get(), self.cat.get(), self.pag.get(), self.pub.get(), self.pca.get())
        self.close_windows()


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
        self.newWindow.resizable(False, False)
        self.app = RentBook(self.newWindow)

    def return_book(self):
        print("Returning book")
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.resizable(False, False)
        self.app = ReturnBook(self.newWindow)

    def check_avail_books(self):
        print("Checking available books")
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.resizable(False, False)
        self.app = CheckAvailability(self.newWindow)


class RentBook(StandardWindow):
    def __init__(self, master):
        super().__init__(master)
        self.frame3 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        self.frame4 = tk.Frame(self.master, borderwidth=10, bg=default_bg)
        create_books_table(self.frame2)
        self.selection = create_form_row(self.frame3, "Choose a book by ID or Title: ")
        create_button(self.frame4, "Submit", self.rent_book, "w", 0, 0)
        create_button(self.frame4, "Back", self.close_windows, "e", 0, 1)
        self.frame3.pack(fill=tk.BOTH)
        self.frame4.pack(fill=tk.BOTH, side=tk.BOTTOM)

    def rent_book(self):
        # TODO: This needs to invoke update function
        sel = self.selection.get()
        b = utils.get_book(int(sel))
        if isinstance(b, bk.Book):
            print("Title: {}".format(b.title))
            print("Rented by: {}".format(logged_user_id))
            b.rented_by = logged_user_id
        else:
            print("Book id not found. Please try again")

        self.close_windows()


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
        self.newWindow.resizable(False, False)
        self.app = DisplayRented(self.newWindow)


def create_form_row(frame_form, title, strvar=None):
    global i, j
    j = 0
    label = tk.Label(master=frame_form, text=title, bg=default_bg)
    option = ""
    if title == "Password: ":
        option = "*"
    if strvar:
        entry = tk.Entry(master=frame_form, show=option, width=30, textvariable=strvar)
    else:
        entry = tk.Entry(master=frame_form, show=option, width=30)
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
    labels = [(0, "ID", 50), (1, "Type", 50), (2, "Name", 100), (3, "Fine", 50), (4, "DoB", 100), (5, "Address 1", 150),
              (6, "Address 2", 150), (7, "Phone", 100), (8, "Mem_since", 100)]
    tree = ttk.Treeview(frame, selectmode="browse", show='headings', column=("ID", "Type", "Name", "Fine", "DoB", "Address 1", "Address 2", "Phone", "Mem_since"))
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')
    for row in labels:
        tree.heading(row[1], text=row[1])
        tree.column(labels[row[0]][1], width=labels[row[0]][2], stretch="NO")

    for row in utils.users:
        if isinstance(row, usrs.Admin):
            tree.insert("", "end", values=(row.uid, row.utype, row.name))
        elif isinstance(row, usrs.Regular):
            tree.insert("", "end", values=(row.uid, row.utype, row.name, row.curr_fine, row.dob, row.addr1, row.addr2, row.phone, row.mem_since))
        else:
            print("Type not recognized")

    tree.pack()


def create_books_table(frame):
    print("Creating books table")
    labels = [(0, "ID", 50), (1, "Title", 250), (2, "Author", 150), (3, "Category", 100),
              (4, "Pages", 50), (5, "Publisher", 150), (6, "Price", 50)]
    headings = ["ID", "Title", "Author", "Category", "Pages", "Publisher", "Price"]
    print(logged_user_type)
    if logged_user_type == "admin":
        labels.append((7, "Rented by", 100))
        headings.append("Rented by")

    # print(labels)
    # print(headings)

    tree = ttk.Treeview(frame, selectmode="browse", show='headings', column=headings)
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')

    for row in labels:
        tree.heading(row[1], text=row[1])
        tree.column(labels[row[0]][1], width=labels[row[0]][2], stretch="NO")

    for row in utils.books:
        tree.insert("", "end", values=(row.bid, row.title, row.author, row.category, row.pages, row.publisher, row.price_cat))

    tree.pack()


def show_message(label, msg):
    label.config(text=msg)


def clear_input(entry):
    entry.delete(0, tk.END)


def zero_the_counters():
    global i, j
    i = 0
    j = 0

# TODO: Add cascade close of all sub-windows when user hits 'log out'

def main():
    # global image
    root = tk.Tk()
    root.resizable(False, False)
    utils.initialise_library()
    # image = tk.PhotoImage(file="logout-1.gif")
    root.title("Library App")
    app = LogInWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
