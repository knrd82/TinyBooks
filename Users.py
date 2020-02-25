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
        return "{:<6}{:<8}{:<20}".format(self.uid, self.utype, self.name)


class Regular(User):
    def __init__(self, *args):
        super(Regular, self).__init__(self, *args)
        self.utype = "user"
        self.name = args[0]
        self.login = args[1]
        self.passwd = args[2]
        self.curr_fine = args[3]
        self.dob = args[4]
        self.addr1 = args[5]
        self.addr2 = args[6]
        self.phone = args[7]
        self.mem_since = args[8]

    def __str__(self):
        return "{:<6}{:<8}{:<20}{:<4}{:<12}{:<32}{:<20}{:<17}{:<15}".format(self.uid, self.utype, self.name, self.curr_fine,
                                                                             self.dob, self.addr1, self.addr2, self.phone,
                                                                             self.mem_since)

