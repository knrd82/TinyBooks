import csv
import Users as usr

USERS_FILE_PATH = "users-csv.csv"
BOOKS_FILE_PATH = "books.csv"

users = []
books = []


def initialise_library():
    print("Initialising Library App")
    read_users_from_csv()
    read_books_from_csv()
    show_all_users()
    print(get_user(1003))
    print(get_user(9999))


def close_library():
    print("Closing Library App")
    update_csv_files()


def read_users_from_csv():
    print("Reading users from file...")
    with open(USERS_FILE_PATH, newline="", mode='r', encoding="utf-8-sig") as userscsv:
        reader = csv.reader(userscsv, delimiter=',')
        for row in reader:
            if row[1] == "admin":
                users.append(usr.Admin(name=row[2], login=row[3], passwd=row[4]))
            elif row[1] == "user":
                users.append(usr.Regular(row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
            else:
                print("User type not recognised")


def read_books_from_csv():
    print("Reading from books csv")


def show_all_users():
    print("Priniting all users")
    print("-" * 60)
    for us in users:
        print(us)


def update_csv_files():
    print("Updating csv files")


def get_user(uid):
    print("Getting user with id: {}".format(uid))
    for us in users:
        if us.uid == uid:
            return us
    return False


def get_book(bid):
    print("Getting book with id: {}".format(bid))


def is_empty():
    print("Checking if list is empty")


def round_up():
    print("Rounding up")
