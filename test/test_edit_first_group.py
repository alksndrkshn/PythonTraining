from model.group import Group
def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="empty_name"))
    app.group.edit_first_group(Group(name="edit name group"))

def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="empty_header"))
    app.group.edit_first_group(Group(header="edit header group"))