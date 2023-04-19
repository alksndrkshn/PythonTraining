from model.contact import Contact
from random import randrange

def test_edit_first_contact(app, db, check_ui):
    if app.contact.get_count() == 0:
        app.contact.create_new(Contact(firstname="empty_contact"))
    old_contacts = db.get_contact_list()
    random_contact = randrange(len(old_contacts))
    contact = Contact(firstname="random_first", middlename="random_middle", nickname="random_nick")
    contact.id = old_contacts[random_contact].id
    contact.lastname = old_contacts[random_contact].lastname
    app.contact.edit_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[random_contact] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
