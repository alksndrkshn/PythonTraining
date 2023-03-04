from model.group import Group
def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edit", header="4321", footer="4321"))
    app.session.logout()