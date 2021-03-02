class User():

    def __init__(self, usrname, pwd, privilege, del_privs, select_privs):
        self.username = usrname
        self.password = pwd
        self.privileges = privilege
        self.tbls_del = del_privs
        self.tbls_sel = select_privs


    def can_create(self):
        if self.privileges.get('Create_User') == True:
            return True
        return False

    def can_delete(self):
        if self.privileges.get('Delete_Tbl') == True:
            return True
        return False

    def can_del_tbl(self, table):
        print("Can delete rows from ", table, " as ", self.username)
        if table in self.tbls_del:
            return True
        return False

    def can_sel_tbl(self, table):
        print("Can select ", table, " as ", self.username)
        if table in self.tbls_sel:
            return True
        return False