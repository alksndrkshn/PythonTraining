from model.group import Group
def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="edit name group"))

def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="edit header group"))