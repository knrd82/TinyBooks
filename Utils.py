from tempfile import NamedTemporaryFile
import shutil
import csv
import Users as usr
import Book as bk

USERS_FILE_PATH = "users-csv.csv"
BOOKS_FILE_PATH = "books.csv"

usersTempFile = NamedTemporaryFile('w+t', newline='', delete=False)
booksTempFile = NamedTemporaryFile('w+t', newline='', delete=False)

users = []
books = []


def initialise_library():
    # TODO: Create updateBook function
    # TODO: Create updateUser function
    # TODO: ERROR - File fails to initialise after 2-3 app launches
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 582: invalid continuation byte

    print("Initialising Library App")
    read_users_from_csv()
    read_books_from_csv()
    # show_all_users()


def close_library():
    print("Closing Library App")
    update_csv_files()


def read_users_from_csv():
    # TODO: This function should read users into temporary file
    print("Reading users from file...")
    with open(USERS_FILE_PATH, newline="", mode='r', encoding="utf-8-sig") as userscsv, usersTempFile:
        reader = csv.reader(userscsv, delimiter=',')
        writer = csv.writer(usersTempFile, delimiter=',')
        for row in reader:
            writer.writerow(row)
            if row[1] == "admin":
                users.append(usr.Admin(name=row[2], login=row[3], passwd=row[4]))
            elif row[1] == "user":
                users.append(usr.Regular(row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
            else:
                print("User type not recognised")

        # print("Users file read: " + writer)


def add_user(type, *args):
    # TODO: Add check if the entry already exists then delete it, otherwise just add
    if type == "Admin":
        ad = usr.Admin(name=args[0], login=args[1], passwd=args[2])
        users.append(ad)
        with open(USERS_FILE_PATH, 'a') as csvfile:
            print("{},{},{},{},{}".format(ad.uid, ad.utype, ad.name, ad.login, ad.passwd), file=csvfile, flush=True)
    elif type == "User":
        us = usr.Regular(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8])
        users.append(us)
        with open(USERS_FILE_PATH, 'a') as csvfile:
            print("{},{},{},{},{},{},{},{},{},{},{}".format(us.uid, us.utype, us.name, us.login, us.passwd,
                                                            us.curr_fine, us.dob, us.addr1, us.addr2, us.phone,
                                                            us.mem_since), file=csvfile, flush=True)
    else:
        print("User type not recognised")


def read_books_from_csv():
    # TODO: This function should read books into temporary file
    print("Reading books from file...")
    with open(BOOKS_FILE_PATH, newline="", mode='r', encoding="utf-8-sig") as bookscsv:
        reader = csv.reader(bookscsv, delimiter=',')
        for row in reader:
            books.append(bk.Book(row[1], row[2], row[3], row[4], row[5], row[6]))


def add_book(*args):
    book = bk.Book(args[0], args[1], args[2], args[3], args[4], args[5])
    books.append(book)
    with open(BOOKS_FILE_PATH, 'a') as bookscsv:
        print("{},{},{},{},{},{},{},{}".format(book.bid, book.title, book.author, book.category, book.pages, book.publisher,
                                            book.price_cat, book.rented_by), file=bookscsv, flush=True)


def show_all_users():
    print("Priniting all users")
    print("-" * 60)
    for us in users:
        print(us)


def update_csv_files():
    # TODO: This function should copy temporary files over to final files and save them
    print("Updating csv files")
    shutil.move(usersTempFile.name, USERS_FILE_PATH)
    # update_file(BOOKS_FILE_PATH, )


def get_user(uid=None, login=None):
    for us in users:
        print("User ID: {}".format(us.uid))
        if us.uid == uid or us.login == login:
            return us
    return False


def get_book(book_id):
    for b in books:
        if b.bid == book_id:
            return b
    return False


def update_file(path, change):
    tempfile = NamedTemporaryFile('w+t', newLine='', delete=False)

    with open(path, mode='rb', encoding="utf-8-sig") as old_file, tempfile:
        reader = csv.reader(old_file, delimiter=',')
        writer = csv.writer(tempfile, delimiter=',')

        for row in reader:
            # TODO: Finish this function
            print("Reading from file: ")
            print(reader)


def is_empty():
    print("Checking if list is empty")


def round_up():
    print("Rounding up")
