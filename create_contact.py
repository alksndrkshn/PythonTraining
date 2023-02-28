# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from aplication import Aplication

@pytest.fixture
def app(request):
    fixture = Aplication()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_create_contact(app):
        app.open_home_page()
        app.login(username="admin", password="secret")
        app.init_create_new_contact()
        app.fill_form(Contact(firstname="Alex", middlename="Smith", nickname="AlSmit"))
        app.submit_create_new_contact()
        app.logout()
def test_create_empty_contact(app):
        app.open_home_page()
        app.login(username="admin", password="secret")
        app.init_create_new_contact()
        app.fill_form(Contact(firstname="", middlename="", nickname=""))
        app.submit_create_new_contact()
        app.logout()

