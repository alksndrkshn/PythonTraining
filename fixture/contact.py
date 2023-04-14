from model.contact import Contact
from selenium.webdriver.support.ui import Select

import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def init_create_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_form(self, contact):
        wd = self.app.wd
        self.change_contact_field("firstname", contact.firstname)
        self.change_contact_field("middlename", contact.middlename)
        self.change_contact_field("lastname", contact.lastname)
        self.change_contact_field("nickname", contact.nickname)
        self.change_contact_field("title", contact.title)
        self.change_contact_field("company", contact.company)
        self.change_contact_field("address", contact.address)
        self.change_contact_field("home", contact.homephone)
        self.change_contact_field("mobile", contact.mobilephone)
        self.change_contact_field("work", contact.workphone)
        self.change_contact_field("email", contact.email1)
        self.change_contact_field("email2", contact.email2)
        self.change_contact_field("email3", contact.email3)
        self.change_contact_field("homepage", contact.site)
        self.change_contact_field("address2", contact.address2)
        self.change_contact_field("phone2", contact.secondaryphone)
        self.change_contact_field("notes", contact.notes)

    def change_contact_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_contact_date(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def submit_create_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='submit']").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_list()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_form(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def submit_edit_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_contact_list(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def create_new(self, contact):
        wd = self.app.wd
        self.init_create_new_contact()
        self.fill_form(contact)
        self.submit_create_new_contact()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def is_list_empty(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_list()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("[name=entry]"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_tag_name("td")
                lastname = element.find_element_by_xpath("./td[2]").text
                firstname = element.find_element_by_xpath("./td[3]").text
                address = element.find_element_by_xpath("./td[4]").text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname,
                                                  address=address, all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def count(self):
        wd = self.app.wd
        self.open_contact_list()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_list()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_view_index(self, index):
        wd = self.app.wd
        self.open_contact_list()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        middlename = wd.find_element_by_name("middlename").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, firstname=firstname, middlename=middlename, lastname=lastname,
                       address=address, homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                       secondaryphone=secondaryphone, email1=email1, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone,
                       mobilephone=mobilephone,
                       workphone=workphone,
                       secondaryphone=secondaryphone)
