from sys import maxsize
class Contact:

    def __init__(self, firstname=None,
                 middlename=None,
                 nickname=None,
                 id=None,
                 all_phones_from_home_page=None,
                 lastname=None,
                 homephone=None,
                 mobilephone=None,
                 workphone=None,
                 secondaryphone=None):
        self.firstname = firstname
        self.middlename = middlename
        self.nickname = nickname
        self.id = id
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page=all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname,  self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
            and self.firstname == other.firstname\
            and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize