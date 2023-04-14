from model.contact import Contact
import random


testdata = [Contact(firstname=random_string(10), middlename=random_string(10),
                    lastname=random_string(10), nickname=random_string(10),
                    title=random_string(10), company=random_string(10),
                    address=random_address(), homephone=random_phone(),
                    mobilephone=random_phone(), workphone=random_phone(), email1=random_email(),
                    email2=random_email(), email3=random_email(),
                    site=random_site(), address2=random_address(),
                    secondaryphone=random_phone(), notes=random_string(20)) for i in range(1)]
