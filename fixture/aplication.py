from selenium import webdriver
from fixture.session_contact import SessionHelper
from fixture.contact import ContactHelper


class Aplication:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session_contact = SessionHelper(self)
        self.contact = ContactHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()