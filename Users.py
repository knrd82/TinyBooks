import csv
import itertools as it


class User:
    uid_iter = it.count(1000, 1)

    def __init__(self, *args, **kwargs):
        self.uid = next(self.uid_iter)
        self.name = kwargs.get("name")
        self.login = kwargs.get("login")
        self.passwd = kwargs.get("passwd")

    def __str__(self):
        return "{:<6}{:<10}".format(self.uid, self.name)


class Admin(User):
    def __init__(self, *args, **kwargs):
        super(Admin, self).__init__(*args, **kwargs)
        self.utype = "admin"

    def __str__(self):
        return "{:<6}{:<10}{:<10}".format(self.uid, self.name, self.utype)


class Regular(User):
    def __init__(self, *args):
        super(Regular, self).__init__(self, *args)
        self.utype = "user"
        self.curr_fine = 0.0
        self.name = args[0]
        self.login = args[1]
        self.passwd = args[2]
        self.dob = args[3]
        self.addr1 = args[4]
        self.addr2 = args[5]
        self.phone = args[6]
        self.mem_since = args[7]

    def __str__(self):
        return "{:<6}{:<10}{:<10}{:<5}{:<15}{:<20}{:<20}{:<12}{:<12}".format(self.uid, self.name, self.utype, self.curr_fine,
                                                                             self.dob, self.addr1, self.addr2, self.phone,
                                                                             self.mem_since)

