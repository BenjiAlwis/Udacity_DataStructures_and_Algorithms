
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
    
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if len(user) == 0 or group is None:
        return False
    if len(user) == 0 or group=='':
        return False
    if user in group.get_users():
        return True
    if len(group.groups) == 0:
        return False
    for grp in group.get_groups():
        fnd=is_user_in_group(user, grp)
        if fnd:
             return True
    return False

parent = Group("parent")
parent.add_user('parent_user')
child = Group("child")
#child.add_user('child_user')
sub_child = Group("subchild")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(user='parent_user', group=parent))
#True
print(is_user_in_group(user='child_user', group=parent))
#False
print(is_user_in_group(user='sub_child_user', group=sub_child))
#True
print(is_user_in_group(user='sub_child_user', group=parent))
#True

#Edge Cases
print(is_user_in_group(user='', group=parent))
#False
print(is_user_in_group(user='sub_child_user', group=None))
#False
print(is_user_in_group(user='xxxxx', group=parent))
#False
print(is_user_in_group(user='xxxxx', group=''))
#False
