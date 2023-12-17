# import database module
import database
import csv
# define a funcion called initializing

Database_obj = database.Database()
def initializing():
    data_temp = database.read_csv("persons.csv").read()
    data_temp2 = database.read_csv("login.csv").read()
    data_temp3 = database.read_csv("project.csv").read()
    data_temp4 = database.read_csv("advisor_pending_request.csv").read()
    data_temp5 = database.read_csv("member_pending_request.csv").read()

    table_persons = database.Table("persons", data_temp)
    table_login = database.Table("login", data_temp2)
    table_project = database.Table("project", data_temp3)
    table_advisor_pending_request = database.Table("advisor_pending_request", data_temp4)
    table_member_pending_request = database.Table("member_pending_request", data_temp5)

    Database_obj.insert(table_persons)
    Database_obj.insert(table_login)
    Database_obj.insert(table_project)
    Database_obj.insert(table_advisor_pending_request)
    Database_obj.insert(table_member_pending_request)
    return Database_obj
    # here are things to do in this function:

    # create an object to read all csv files that will serve as a persistent state for this program

    # create all the corresponding tables for those csv files

    # see the guide how many tables are needed

    # add all these tables to the database


# define a funcion called login

def login():
    user = input("Username: ")
    pwd = input("Password: ")
    data = Database_obj.search("login.csv")
    for i in data:
        if (i['username']) == user and (i['password']) == pwd:
            return (i['ID']), (i['role'])
        else:
            return None


# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [ID, role] if valid, otherwise returning None

# define a function called exit
def exit(data_b):
    for tables in data_b.database:
        myfile = open(tables.Table.table_name, 'w')
        writer = csv.writer(myfile)
        writer.writerow([tables.table])
        for dictionary in Database_obj.database:
            writer.writerow(dictionary.values())
        myfile.close()
        myfile = open(tables.Table.table_name, 'r')
        print(f"The content of the {tables.Table.table_name} is:")
        print(myfile.read())
        myfile.close()


# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
   
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

data_base = initializing()
val = login()
while val is None:
    print("Username or password is invalid.")
    val = login()
end = True
while end:
# based on the return value for login, activate the code that performs activities according to the role defined for that person_id
    if val[1] == 'admin':
        person = database.Persons('admin', val[0], data_base)
        capable = person.capable()
        choose = person.choose()
        end = choose
      # see and do admin related activities
    elif val[1] == 'student':
        person = database.Persons('student', val[0], data_base)
        capable = person.capable()
        choose = person.choose()
        end = choose
      # see and do student related activities
    elif val[1] == 'member':
        person = database.Persons('member', val[0], data_base)
        capable = person.capable()
        choose = person.choose()
        end = choose
      # see and do member related activities
    elif val[1] == 'lead':
        person = database.Persons('lead', val[0], data_base)
        capable = person.capable()
        choose = person.choose()
        end = choose
      # see and do lead related activities
    elif val[1] == 'faculty':
        person = database.Persons('faculty', val[0], data_base)
        capable = person.capable()
        choose = person.choose()
        end = choose
      # see and do faculty related activities
    elif val[1] == 'advisor':
        person = database.Persons('advisor', val[0], data_base)
        capable = person.capable()
        choose = person.choose()
        end = choose
      # see and do advisor related activities

# once everyhthing is done, make a call to the exit function
print(Database_obj)
exit(data_base)

