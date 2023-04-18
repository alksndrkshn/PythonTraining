# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact


def test_create_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create_new(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                             key=Contact.id_or_max)

# def test_create_empty_contact(app):
#        app.open_home_page()
#        app.contact.init_create_new_contact()
#        app.contact.fill_form(Contact(firstname="", middlename="", nickname=""))
#        app.contact.submit_create_new_contact()
