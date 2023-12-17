# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv, os, copy
class read_csv:
    def __init__(self, name):
        self.data = []
        self.file_name = name

    def read(self):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

        with open(os.path.join(__location__, self.file_name)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.data.append(dict(r))

        return self.data

# add in code for a Database class
class Database:
    def __init__(self):
        self.database = []

    def insert(self, table):
        self.database.append(table)

    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None
# add in code for a Table class
class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def join(self, other_table, common_key):
        joined_table = Table(self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def update_table(self, id_value, key, value):
        for data in self.table:
            if data["ID"] == str(id_value):
                data[key] = value
                return data
        return

    def update_dict(self, id_value):
        for data in self.table:
            if data["ID"] == str(id_value):
                for keys in data.keys():
                    data[keys] = input(f"Enter new {keys}: ")
                return data
        return

class Persons:
    def __init__(self, positions, id, database):
        self.positions = positions
        self.id = id
        self.db = database
        self.name = self.find_name(id)

    def find_name(self, id):
        for i in self.db.search("login.csv").table:
            if i["ID"] == str(id):
                return i["username"]

    def capable(self):
        print(f"Welcome {self.name} :D.")
        print(f"would you like to")
        if self.positions == 'admin':
            print("0. exit.")
            print("1. Update a value.")
            print("2. Update a dictionary.")
        elif self.positions == 'student':
            print("0. exit.")
            print("1. See project invitations.")
            print("2. Respond to invitations.")
            print("** keep in mind that you have to involved least one group project **")
        elif self.positions == 'member':
            print("0. exit.")
            print("1. Modify project.")
        elif self.positions == 'lead':
            print("0. exit.")
            print("1. Create project.")
            print("2. Find members.")
            print("3. Invite students to the project")
            print("4. Modify project.")
            print("5. Request to an advisor.")
            print("6. Submit project to advisors.")
        elif self.positions == 'faculty':
            print("0. exit.")
            print("1. See an advisor requests.")
            print("2. Respond to requests.")
            print("3. See project details.")
            print("4. Evaluate Projects.")
        elif self.positions == 'advisor'
            print("0. exit.")
            print("1. See advisor requests.")
            print("2. Respond to requests.")
            print("3. See project details.")
            print("4. Approve the project.")
            print("5. Evaluate Projects.")

    def choose(self):
        choice = input(f"Enter your choice: ")
        while choice != 0:
            if self.positions == 'admin':
                if choice == 1:
                    

        return False




# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated
