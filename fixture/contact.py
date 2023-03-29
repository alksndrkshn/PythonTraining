from model.contact import Contact
class ContactHelper:

    def __init__(self, app):
        self.app = app


    def init_create_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

    def submit_create_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_form(contact)

    def submit_edit_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

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

    def is_list_empty(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contact_list()
        contacts = []
        for element in wd.find_elements_by_css_selector("[name=entry]"):
            lastname = element.find_element_by_xpath("./td[2]").text
            firstname = element.find_element_by_xpath("./td[3]").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return contacts


