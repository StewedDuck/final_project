import csv
import os
import copy


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

    def update_dict(self, id, key, value):
        for data in self.table:
            if data["ID"] == str(id):
                data[key] = value
                return data
        return None

    def update_values(self, id):
        for data in self.table:
            if data["ID"] == str(id):
                for keys in data.keys():
                    data[keys] = input(f"Enter new {keys}: ")
                return data
        return None


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

    def project_details(self):
        for projects in self.db.search("project.csv").table:
            members = [projects['Lead'], projects['Member1'], projects['Member2']]
            if self.id in members:
                print(f"Your project details:"
                      f"Title: {projects['Title']} ID: {projects['ID']}")
                print(f"Lead: {self.find_name(projects['Lead'])}")
                member1 = self.find_name(projects['Member1'])
                if member1 is not None:
                    print(f"Member1: {member1}")
                elif member1 is None:
                    print(f"Member1: None")
                member2 = self.find_name(projects['Member2'])
                if member2 is not None:
                    print(f"Member2: {member2}")
                elif member2 is None:
                    print(f"Member2: None")
                print(f"Advisor: {self.find_name(projects['Advisor'])}"
                      f"Status: {projects['Status']}"
                      f"Details: {projects['Details']}")
        return False

    def capable(self):
        print(f"Welcome {self.name} ,Your roles is {self.positions} :D.")
        print(f"Would you like to")
        if self.positions == 'admin':
            print("0. exit.")
            print("1. Update a value.")
            print("2. Update a dictionary.")
        elif self.positions == 'student':
            print("0. exit.")
            print("1. See project invitations.")
            print("2. Respond to invitations.")
            print("3. Become a lead students?")
            print("** Keep in mind that you have to involved least one group's project **")
        elif self.positions == 'member':
            print("0. exit.")
            print("1. Modify project.")
            print("** Now that you are in, I'm just wanted to remind you that it no way out :P **")
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
        elif self.positions == 'advisor':
            print("0. exit.")
            print("1. See advisor requests.")
            print("2. Respond to requests.")
            print("3. See project details.")
            print("4. Approve the project.")
            print("5. Evaluate Projects.")

    def choose(self):
        choice = input(int(f"Enter your choice: "))
        while choice != 0:
            if self.positions == 'admin':
                id = input(str("Enter id: "))
                if choice == 1:
                    while True:
                        print("Updating these Tables:")
                        for tables in self.db:
                            print(tables.table_name)
                        print()
                        table = input("Choose the table to update the Values: ")
                        result = self.db.search(table).Table.update_values(id)
                        print("Updated Tables")
                        print(result)
                        continues = input("Continue updating? (Yes/No): ")
                        if continues == "No":
                            break
                        elif continues == "no":
                            break
                elif choice == 2:
                    while True:
                        print("Updating these Tables:")
                        for tables in self.db:
                            print(tables.table_name)
                        print()
                        table = input("Choose the table to update: ")
                        key = input("Enter key: ")
                        data = input("Enter data: ")
                        result = self.db.search(table).Table.update_dict(id, key, data)
                        print("Updated Tables")
                        print(result)
                        continues = input("Continue updating? (Yes/No): ")
                        if continues == "No":
                            return None
                        elif continues == "no":
                            return None
            elif self.positions == 'student':
                if choice == 1:
                    for invited in self.db.search("member_pending_request.csv").table:
                        if str(self.id) == invited["Member"]:
                            for projects in self.db.search("project.csv").table:
                                if projects["ID"] == invited['ID']:
                                    print("You have invited!! :D ")
                                    print("Here are your invitation")
                                    print(f"Project ID: {invited['ID']} "
                                          f"Title: {projects['Title']}")
                                else:
                                    print("You have no invitation :( ")
                elif choice == 2:
                    temp_list = []
                    print("Select projects to join.")
                    for invite in self.db.search("member_pending_request.csv").table:
                        if str(self.id) == invite["Member"]:
                            if invite["Response"] == "waiting for response":
                                print(f"Project ID: {invite['ID']}")
                                temp_list.append(invite["ID"])
                            print("Not found.")
                            return None
                    project = input("Enter project ID : ")
                    while project not in temp_list:
                        print("Invalid project ID")
                        project = input("Enter project ID : ")
                    for invite in self.db.search("member_pending_request.csv").table:
                        if str(self.id) == invite["Member"]:
                            if project == invite["ID"]:
                                invite["Response"] = "waiting for confirmation"
                    print(self.db.search("member_pending_request.csv"))
                elif choice == 3:
                    print("Become a lead students?")
                    answer = input("(yes/no): ")
                    while answer != "yes" and answer != "no":
                        print("Invalid choice.")
                        answer = input("(yes/no): ")
                    if answer == "yes":
                        for user in self.db.search("persons.csv").table:
                            if user["ID"] == str(self.id):
                                self.positions = 'lead'
                                user["type"] = "lead"
                        for user in self.db.search("login.csv").table:
                            if user["ID"] == str(self.id):
                                self.positions = 'lead'
                                user["role"] = "lead"
            elif self.positions == 'member':
                self.project_details()
                print("Modifying project details.")
                for project in self.db.search("project.csv").table:
                    if str(self.id) in project["Member1"] or str(self.id) in project['Member2']:
                        details = input("Enter details: ")
                        project["Details"] = details
                        print("After Modified project details.")
                        self.project_details()
            elif self.positions == 'lead':
                if choice == 1:
                    temp_dict = {}
                    for _ in self.db.search("project.csv").table:
                        title = input("Enter project title: ")
                        detail = input("Enter details: ")
                        temp_dict.update({"Title": title})
                        temp_dict.update(({"Lead": f"{self.id}"}))
                        temp_dict.update({"Member1": "None"})
                        temp_dict.update({"Member2": "None"})
                        temp_dict.update({"Details": detail})
                        temp_dict.update({"Advisor": "None"})
                        temp_dict.update({"Status": "None"})
                        self.db.search("Projects.csv").insert([temp_dict])
                        print("Here is your brand new Project.")
                        self.project_details()
                elif choice == 2:
                    print("Students lists that aren't in any group yet.")
                    for students in self.db.search("persons.csv").table:
                        if students["ID"] not in self.db.search("project.csv").table:
                            print(f"Name: {students['first']} {students['last']} ID: {students['ID']}")
                elif choice == 3:
                    print("Inviting students to project.")
                    id = input("Enter student ID: ")
                    request = {}
                    for students in self.db.search("persons.csv").table:
                        if id in students["ID"]:
                            if students["type"] == "student":
                                for projects in self.db.search("project.csv").table:
                                    if str(self.id) in projects["Lead"]:
                                        request.update({"ID": projects["ID"]})
                                        request.update({"Member": id})
                                        request.update({"Response": "waiting for response"})
                                        self.db.search("member_pending_request.csv").insert([request])
                                        print("Request sent")
                        elif id not in self.db.search("persons.csv").table:
                            print("ID is invalid.")
                        return None
                elif choice == 4:
                    self.project_details()
                    print("Updating details.")
                    for project in self.db.search("project.csv").table:
                        if str(self.id) in project["Lead"]:
                            details = input("Enter details: ")
                            project["Details"] = details
                            print("After Modified project details.")
                            self.project_details()
                            return None
                elif choice == 5:
                    temp_list = []
                    print("List of Faculty: ")
                    for faculty in self.db.search("persons.csv").table:
                        if faculty["type"] in ["faculty"]:
                            temp_list.append(faculty)
                            print(f"Name: {faculty['first']} {faculty['last']} ID: {faculty['ID']}")
                    print("Enter a ID from the list to invite an faculty to become an Advisor")
                    id = input(str("Enter ID: "))
                    temp_dict = {}
                    for faculty in self.db.search("persons.csv").table:
                        if id in faculty["ID"]:
                            if faculty["type"] == "Faculty":
                                for facultys in self.db.search("project.csv").table:
                                    temp_dict.update({"ID": facultys["ID"]})
                                    temp_dict.update({"Advisor": f"{faculty['first']} {faculty['last']}"})
                                    temp_dict.update({"Response": "waiting for response"})
                                    self.db.search("advisor_pending_request.csv").insert([temp_dict])
                                    print("Request sent")
                elif choice == 6:
                    for projects in self.db.search("Projects.csv").table:
                        if projects["Status"] == "during proposal":
                            print("Submitting the proposal.")
                            submit = input("Submit? (yes/no): ")
                            while submit != "yes" and submit != "no":
                                print("Invalid choice.")
                                submit = input("Submit? (yes/no): ")
                            if submit == "yes":
                                print("project proposal submitted.")
                                projects["Status"] = "waiting for the proposal approval"
                                return None
                            else:
                                print("Cancel.")
                                return None
                        if projects["Status"] == "approving":
                            print("Waiting for approval.")
                            return
                    print("Submitting for the final approval.")
                    submit = input("Submit? (yes/no): ")
                    while submit != "yes" and submit != "no":
                        print("Invalid choice.")
                        submit = input("Submit? (yes/no): ")
                    if submit == "yes":
                        print("Project submitted.")
                        temp_dict = {}
                        for projects in self.db.search("project.csv").table:
                            if str(self.id) in projects["Lead"]:
                                projects["Status"] = "Evaluating"
                                temp_dict.update({"ID": projects["ID"]})
                                temp_dict.update({"Title": projects["Title"]})
                                temp_dict.update({"comments": []})
                                temp_dict.update({"evaluators": projects["Advisor"]})
                                temp_dict.update({"score": "processing"})
                                self.db.search("project.csv").table.insert(temp_dict)
                    elif choice == "no":
                        print("Cancel.")
                        return None
            elif self.positions == 'faculty':
                if choice == 1:
                    for invited in self.db.search("advisor_pending_request.csv").table:
                        if str(self.id) == invited["Advisor"]:
                            for projects in self.db.search("project.csv").table:
                                if projects["ID"] == invited['ID']:
                                    print("You have invited!! :D ")
                                    print("Here are your invitation")
                                    print(f"Project ID: {invited['ID']} "
                                          f"Title: {projects['Title']}")
                                else:
                                    print("You have no invitation :( ")
                elif choice == 2:
                    temp_list = []
                    print("Select projects to join.")
                    for invite in self.db.search("advisor_pending_request.csv").table:
                        if str(self.id) == invite["Advisor"]:
                            if invite["Response"] == "waiting for response":
                                print(f"Project ID: {invite['ID']}")
                                temp_list.append(invite["ID"])
                            print("Not found.")
                            return None
                    project = input("Enter project ID : ")
                    while project not in temp_list:
                        print("Invalid project ID")
                        project = input("Enter project ID : ")
                    for invite in self.db.search("member_pending_request.csv").table:
                        if str(self.id) == invite["Advisor"]:
                            if project == invite["ID"]:
                                invite["Response"] = "waiting for confirmation"
                    print(self.db.search("member_pending_request.csv"))
                elif choice == 3:
                    print("List of projects:")
                    if len(self.db.search("project.csv").table) == 0:
                        print("No projects found.")
                    for projects in self.db.search("project.csv").table:
                        print(f'ID: {projects["ID"]} Title: {projects["Title"]}')
                        print(f"Lead: {self.find_name(projects['Lead'])}")
                        member1 = self.find_name(projects['Member1'])
                        member2 = self.find_name(projects['Member2'])
                        if member1 is not None:
                            print(f"Member1: {member1}")
                        elif member1 is None:
                            print(f"Member1: None")
                        if member2 is not None:
                            print(f"Member2: {member2}")
                        elif member2 is None:
                            print(f"Member2: None")
                elif choice == 4:
                    temp_dict = {}
                    score = input("pass or not :(PASS/N)")
                    comment = input("Comment: ")
                    for items in self.db.search("project.csv").table:
                        items["Status"] = "Evaluated"
                        temp_dict.update({"ID": items["ID"]})
                        temp_dict.update({"Title": items["Title"]})
                        temp_dict.update({"score": score})
                        temp_dict.update(({"comments": comment}))
                        temp_dict.update({"evaluators": items["Advisor"]})
                        self.db.search("project.csv").table.insert(temp_dict)
            elif self.positions == 'advisor':
                if choice == 1:
                    for invited in self.db.search("advisor_pending_request.csv").table:
                        if str(self.id) == invited["Advisor"]:
                            for projects in self.db.search("project.csv").table:
                                if projects["ID"] == invited['ID']:
                                    print("You have invited!! :D ")
                                    print("Here are your invitation")
                                    print(f"Project ID: {invited['ID']} "
                                          f"Title: {projects['Title']}")
                                else:
                                    print("You have no invitation :( ")
                elif choice == 2:
                    temp_list = []
                    print("Select projects to join.")
                    for invite in self.db.search("advisor_pending_request.csv").table:
                        if str(self.id) == invite["Advisor"]:
                            if invite["Response"] == "waiting for response":
                                print(f"Project ID: {invite['ID']}")
                                temp_list.append(invite["ID"])
                            print("Not found.")
                            return None
                    project = input("Enter project ID : ")
                    while project not in temp_list:
                        print("Invalid project ID")
                        project = input("Enter project ID : ")
                    for invite in self.db.search("member_pending_request.csv").table:
                        if str(self.id) == invite["Advisor"]:
                            if project == invite["ID"]:
                                invite["Response"] = "waiting for confirmation"
                    print(self.db.search("member_pending_request.csv"))
                elif choice == 3:
                    print("List of projects:")
                    if len(self.db.search("project.csv").table) == 0:
                        print("No projects found.")
                    for projects in self.db.search("project.csv").table:
                        print(f'ID: {projects["ID"]} Title: {projects["Title"]}')
                        print(f"Lead: {self.find_name(projects['Lead'])}")
                        member1 = self.find_name(projects['Member1'])
                        member2 = self.find_name(projects['Member2'])
                        if member1 is not None:
                            print(f"Member1: {member1}")
                        elif member1 is None:
                            print(f"Member1: None")
                        if member2 is not None:
                            print(f"Member2: {member2}")
                        elif member2 is None:
                            print(f"Member2: None")
                elif choice == 4:
                    temp_dict = {}
                    approve = input("pass or not :(PASS/N)")
                    comment = input("Comment: ")
                    for items in self.db.search("project.csv").table:
                        items["Status"] = "Approved"
                        temp_dict.update({"Approval": approve})
                        temp_dict.update(({"comments": comment}))
                        temp_dict.update({"evaluators": items["Advisor"]})
                        self.db.search("project.csv").table.insert(temp_dict)
                elif choice == 5:
                    temp_dict = {}
                    score = input("pass or not :(PASS/N)")
                    comment = input("Comment: ")
                    for items in self.db.search("project.csv").table:
                        items["Status"] = "Evaluated"
                        temp_dict.update({"ID": items["ID"]})
                        temp_dict.update({"Title": items["Title"]})
                        temp_dict.update({"score": score})
                        temp_dict.update(({"comments": comment}))
                        temp_dict.update({"evaluators": items["Advisor"]})
                        self.db.search("project.csv").table.insert(temp_dict)
        return False
