from sys import maxsize
class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, id=None,
                 all_phones_from_home_page=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None,
                 title=None, company=None, address=None, email1=None, email2=None, email3=None,
                 site=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None,
                 ayear=None, address2=None, notes=None,
                 all_emails_from_home_page=None
                 ):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.id = id
        self.title = title
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.company = company
        self.address = address
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.site = site
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.notes = notes
        self.all_emails_from_home_page = all_emails_from_home_page

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