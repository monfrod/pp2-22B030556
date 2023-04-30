import psycopg2

import csv

from database import conn

from all_function import *

def start():
    running = True
    while running:
        a = int(input("""
1. Add contact
2. Delete contact
3. Add phone number for contact
4. Print all contacts
5. Print all Phone numbers
6. Get contact by id
7. Get phone number by id
8. Update contact
9. Update phone number
10. Add contacts from csv
11. Add phone numbers from csv
12. Exit"""))
        if a == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            create_contact(name, email)
        if a == 2:
            contact_id = input("Enter contact id: ")
            delete_contact(contact_id)
        if a == 3:
            number = input("Enter number: ")
            contact_id = input("Enter contact id: ")
            create_phone_number(contact_id, number)
        if a == 4:
            data = get_all_contacts()
            print()
            print("id   Name   Email")
            for i in data:
                print(i[0], "  ", i[1], "  ", i[2])
        if a == 5:
            data = get_all_phone_numbers()
            print()
            print("id   Phone   contact_id")
            for i in data:
                print(i[0], "  ", i[1], "  ", i[2])
        if a == 6:
            contact_id = input("Enter contact id: ")
            data = get_contact(contact_id)
            print("id   Name   Email")
            print(data[0], "  ", data[1], "  ", data[2])
        if a == 7:
            id = input("Enter id of phone number: ")
            data = get_phone_numbers(id)
            print(data)
            print("id   Phone   contact_id")
            print(data[0][0], "  ", data[0][1], "  ", data[0][2])
        if a == 8:
            id = input("Enter id of contact: ")
            name = input("Enter a name: ")
            email = input("Enter email: ")
            update_contact(id, name, email)

        if a == 9:
            id = input("Enter id of phone number: ")
            number = input("Enter a number: ")
            update_phone_number(id, number)

        if a == 10:
            with open("myFile0.csv") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        cur.execute("INSERT INTO contacts (id, name, email) VALUES (%s, %s, %s)",
                                    (row['id'], row['name'], row['email']))
                    except errors.UniqueViolation as e:
                        print(e)
                    conn.commit()

        if a == 11:
            with open("myFile1.csv") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    try:
                        cur.execute("INSERT INTO phone_numbers (id, number, contact_id) VALUES (%s, %s, %s)",
                                    (row['id'], row['number'], row['contact_id']))
                    except errors.UniqueViolation as e:
                        print(e)
                    except errors.ForeignKeyViolation as e:
                        print(e)

                    conn.commit()

        if a == 12:
            running = False
        conn.commit()
if __name__ == '__main__':
    start()
