from model.contact import Contact
from random import randrange
def test_delete_some_contact(app):
    if app.contact.is_list_empty() == 0:
        app.contact.create_new(Contact(firstname="empty_contact", middlename="empty_contact", nickname="empty_contact"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)