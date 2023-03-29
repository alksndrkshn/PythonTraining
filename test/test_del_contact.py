from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.is_list_empty() == 0:
        app.contact.create_new(Contact(firstname="empty contact", middlename="empty contact", nickname="empty contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts