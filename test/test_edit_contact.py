from model.contact import Contact
from random import randrange
def test_edit_first_contact(app):
    if app.contact.is_list_empty() == 0:
        app.contact.create_new(Contact(firstname="empty_contact", middlename="empty_contact", nickname="empty_contact"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    new_contact = Contact(firstname="random_first", middlename="random_middle", nickname="random_nick")
    new_contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, new_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
