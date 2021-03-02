class Group():

    def __init__(self, name, privilege, delete_priv, select_priv):
        self.name = name
        self.privileges = privilege
        self.tbls_del = delete_priv
        self.tbls_sel = select_priv
        self.users = set()

    def add_user(self, user):
        self.users.add(user)
        user.privileges.update(self.privileges)
        for priv in self.tbls_del:
            user.tbls_del.add(priv)
        for priv in self.tbls_sel:
            user.tbls_sel.add(priv)

    def update_privilege(self, privilege):
        for priv in privilege:
            self.privileges.update({priv: True})
            for user in self.users:
                user.privileges.update({priv: True})

    def update_select_privilege(self, privilege):
        print(privilege)
        self.tbls_sel.add(privilege)
        for user in self.users:
            user.tbls_sel.add(privilege)

    def update_delete_privilege(self, privilege):
        print(privilege)
        self.tbls_del.add(privilege)
        for user in self.users:
            user.tbls_del.add(privilege)