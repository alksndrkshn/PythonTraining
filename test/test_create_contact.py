# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact


def test_create_contact(app):
        app.open_home_page()
        app.contact.init_create_new_contact()
        app.contact.fill_form(Contact(firstname="Alex", middlename="Smith", nickname="AlSmit"))
        app.contact.submit_create_new_contact()

def test_create_empty_contact(app):
        app.open_home_page()
        app.contact.init_create_new_contact()
        app.contact.fill_form(Contact(firstname="", middlename="", nickname=""))
        app.contact.submit_create_new_contact()

