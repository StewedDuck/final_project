import database
import csv
import os


def initializing():
    Database_obj = database.Database()
    for files in os.listdir():
        if files.endswith(".csv"):
            data = database.Table(files, database.read_csv(files).read())
            Database_obj.insert(data)
    return Database_obj


def login(database):
    user = input("Username: ")
    pwd = input("Password: ")
    for i in database.search("login.csv").table:
        if user in i["username"]:
            if pwd in i["password"]:
                return [i["ID"], i["role"]]
    return None


def exit(data_b):
    for tables in data_b.database:
        if len(tables.table) != 0:
            keys = tables.table[0].keys()
            my_file = open(tables.table_name, 'w')
            writer = csv.DictWriter(my_file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(tables.table)
            my_file.close()


data_base = initializing()
val = login(data_base)
while val is None:
    print("Username or password is invalid.")
    val = login(data_base)
end = True
while end:
    id = val[0]
    db = data_base
    if val[1] == 'admin':
        person = database.Persons('admin', id, db)
        capable = person.capable()
        choose = person.choose()
        end = choose
    elif val[1] == 'student':
        person = database.Persons('student', id, db)
        capable = person.capable()
        choose = person.choose()
        end = choose
    elif val[1] == 'member':
        person = database.Persons('member', id, db)
        capable = person.capable()
        choose = person.choose()
        end = choose
    elif val[1] == 'lead':
        person = database.Persons('lead', id, db)
        capable = person.capable()
        choose = person.choose()
        end = choose
    elif val[1] == 'faculty':
        person = database.Persons('faculty', id, db)
        capable = person.capable()
        choose = person.choose()
        end = choose
    elif val[1] == 'advisor':
        person = database.Persons('advisor', id, db)
        capable = person.capable()
        choose = person.choose()
        end = choose
exit(data_base)
