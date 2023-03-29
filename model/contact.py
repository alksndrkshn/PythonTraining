from sys import maxsize
class Contact:

    def __init__(self, firstname=None, middlename=None, nickname=None, id=None, lastname=None):
        self.firstname = firstname
        self.middlename = middlename
        self.nickname = nickname
        self.id = id
        self.lastname = lastname

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.middlename, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
            and self.firstname == other.firstname and self.middlename == other.middlename

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize