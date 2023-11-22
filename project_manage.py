
# import other necessary modules
import database as db
import csv
import os
import random
import string
# create an object to read an input csv file, persons.csv
my_db = db.DB()

# create a 'persons' table
persons_table = db.Table('persons', [])

# add the 'persons' table into the database
csv_file_path = os.path.join(os.getcwd(), 'persons.csv')
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        persons_table.insert_entry(row)

# create a 'login' table
login_table = db.Table('login', [])
my_db.insert(login_table)

# the 'login' table has the following keys (attributes):
# person_id
# username
# password
# role

# a person_id is the same as that in the 'persons' table
# let a username be a person's first name followed by a dot and the first letter of that person's last name
# let a password be a random four digits string
# let the initial role of all the students be Member
# let the initial role of all the faculties be Faculty
# you create a login table by performing a series of insert operations; each insert adds a dictionary to a list
# add the 'login' table into the database
# add code that performs a login task; asking a user for a username and password; returning [person_id, role] if valid, otherwise returning None

# Extract the person IDs and store them in a list
person_ids = [int(person['ID']) for person in persons_table.table]

# Extract the usernames and store them in a list
usernames = [person['fist'] for person in persons_table.table]

# Extract the roles and store them in a list
role = [person["type"] for person in persons_table.table]

# Extract the first character of each last name
last = [person['last'][0] for person in persons_table.table]

# set login table
for i in range(len(person_ids)):
    login_table.insert_entry({'person_id': person_ids[i], 'username': usernames[i] + '.' +
                             last[i], 'password': ''.join(random.choices(string.digits, k=4)), 'role': role[i]})

# login function


def login(username, password):
    for i in range(len(login_table.table)):
        if username == login_table.table[i]['username'] and password == login_table.table[i]['password']:
            return [login_table.table[i]['person_id'], login_table.table[i]['role']]
    return None

### for hint for user name and password you can used the following code###
# print('Hint: username is the first name followed by a dot and the first letter of the last name')
# print('Hint: password is a random four digits string')
# print(login_table.table)


# test login function
access = False
while not access:
    print("Enter username and password to access or 'exit' to exit the program.")
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if login(username, password) != None:
        person_id, role = login(username, password)
        access = True
        print('Access granted.')
    elif username == 'exit' or password == 'exit':
        break
    else:
        print('Access denied.')

print(f"Hello, welcome to the project management system.")
print(f"Your role is {role}.")
