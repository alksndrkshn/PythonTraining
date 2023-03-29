from model.contact import Contact
def test_edit_first_contact(app):
    if app.contact.is_list_empty() == 0:
        app.contact.create_new(Contact(firstname="empty contact", middlename="empty contact", nickname="empty contact"))
    #app.contact.edit_first_contact(Contact(firstname="Aleksnadr", middlename="Sergeevich", nickname="AlSmit1"))
    #app.contact.submit_edit_contact()
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="Aleksnadr", middlename="Sergeevich", nickname="AlSmit1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)