# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
def test_create_contact(app):
        old_contacts = app.contact.get_contact_list()
        contact = Contact(firstname="name_test", middlename="middle_test"Bc, nickname="nick_test")
        app.contact.create_new(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_create_empty_contact(app):
#        app.open_home_page()
#        app.contact.init_create_new_contact()
#        app.contact.fill_form(Contact(firstname="", middlename="", nickname=""))
#        app.contact.submit_create_new_contact()
