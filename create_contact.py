# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from contact import Contact


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_create_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_create_new_contact(wd)
        self.fill_form(wd,Contact(firstname="Alex", middlename="Smith", nickname="AlSmit"))
        self.submit_create_new_contact(wd)
        self.logout(wd)

    def test_create_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_create_new_contact(wd)
        self.fill_form(wd, Contact(firstname="", middlename="", nickname=""))
        self.submit_create_new_contact(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def submit_create_new_contact(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_form(self, wd, contact):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

    def init_create_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("https://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
