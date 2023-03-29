from model.contact import Contact
def test_edit_first_contact(app):
    if app.contact.is_list_empty() == 0:
        app.contact.create_new(Contact(firstname="empty contact", middlename="empty contact", nickname="empty contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="Aleksnadr", middlename="Sergeevich", nickname="AlSmit1"))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
