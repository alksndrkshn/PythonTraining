# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.aplication import Aplication

@pytest.fixture
def app(request):
    fixture = Aplication()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_create_contact(app):
        app.open_home_page()
        app.session_contact.login(username="admin", password="secret")
        app.contact.init_create_new_contact()
        app.contact.fill_form(Contact(firstname="Alex", middlename="Smith", nickname="AlSmit"))
        app.contact.submit_create_new_contact()
        app.session_contact.logout()
def test_create_empty_contact(app):
        app.open_home_page()
        app.session_contact.login(username="admin", password="secret")
        app.contact.init_create_new_contact()
        app.contact.fill_form(Contact(firstname="", middlename="", nickname=""))
        app.contact.submit_create_new_contact()
        app.session_contact.logout()

