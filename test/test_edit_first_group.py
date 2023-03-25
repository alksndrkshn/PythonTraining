from model.group import Group
def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="empty_name"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="edit name group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="empty_header"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="edit header group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)