from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.is_list_empty() == 0:
        app.contact.create_new(Contact(firstname="empty contact", middlename="empty contact", nickname="empty contact"))
    #app.contact.delete_first_contact()
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)