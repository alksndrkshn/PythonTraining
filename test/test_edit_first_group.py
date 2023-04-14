from model.group import Group
from random import randrange
def test_edit_first_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name", header="head", footer="foot"))
    old_groups = db.get_group_list()
    group = Group(name="edited_group_name", header="edited_header", footer="edited_footer")
    random_group = randrange(len(old_groups))
    group.id = old_groups[random_group].id
    app.group.edit_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    old_groups[random_group] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_edit_first_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="empty_header"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_group(Group(header="edit_header_group"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)