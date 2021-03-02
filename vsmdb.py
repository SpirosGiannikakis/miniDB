from database import Database
# create db with name "smdb"
db = Database('vsmdb', load=False)
# create a single table named "classroom"
db.create_table('classroom', ['building', 'room_number', 'capacity'], [str,str,int])
# insert 5 rows
db.insert('classroom', ['Packard', '101', '500'])
db.insert('classroom', ['Painter', '514', '10'])
db.insert('classroom', ['Taylor', '3128', '70'])
db.insert('classroom', ['Watson', '100', '30'])
db.insert('classroom', ['Watson', '120', '50'])


   #Checking Create User
#db.create_user('John', 'Stent')
#db.logout()
#db.login('John', 'Stent')

    #Checking Groups Funtionality
#db.add_user_to_group('viewers', 'John')
#db.logout()
#db.login('John', 'Stent')
#db.select('classroom', ['building'])
#db.logout()
#db.login('admin', 'admin')
#db.add_user_to_group('admins', 'John')
#db.logout()
#db.login('John', 'Stent')
#db.delete('classroom', 'building==Packard')

    #Checking create User and grant privileges
#db.create_user('miniDB', 'miniDB')
#db.grant_create_privilege('John')
#db.grant_delete_privilege('John')
#db.grant_select_table_privileges('John', 'building')
#db.grant_delete_table_privileges('John', 'building')

    #Checking Select Table
#db.select('classroom', ['building'])
#db.logout()
#db.login('admin', 'admin')
#db.select('classroom', ['building'])
#db.grant_select_table_privileges('John', 'classroom')
#db.logout()
#db.login('John', 'Stent')
#db.select('classroom', ['building'])

    #Checking Delete Row
#print("\nChecking Delete Row\n")
#db.delete('classroom', 'building == Packard')
#db.logout()
#db.login('admin', 'admin')
#db.grant_delete_table_privileges('John', 'classroom')
#db.logout()
#db.login('John', 'Stent')
#db.delete('classroom', 'building == Packard')

    #Checking Drop Table
#print("\nChecking Drop Table\n")
#db.drop_table('classroom')
#db.logout()
#db.login('admin', 'admin')
#db.grant_delete_privilege('John')
#db.logout()
#db.login('John', 'Stent')
#db.drop_table('classroom')
#db.select('classroom', ['building'])

