from model.contact import Contact
def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.open_home_page()
    app.contact.edit_first_contact(Contact(firstname="Aleksnadr", middlename="Sergeevich", nickname="AlSmit1"))
    app.contact.submit_edit_contact()
    app.session.logout()