#!/usr/bin/python

import sqlite3


# create a contact class
class Contact():
    def __init__(self,  first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name =  last_name
        self.phone_number = phone_number
        self.email = email

    def get_fname(self):
        return self.first_name
    
    def get_lname(self):
        return self.last_name


class ContactBook():
    def __init__(self):
        pass


"""interacting with database"""
def connect_db(funct):
    def db_execute(*args, **kwargs):
        db_connection = sqlite3.connect("contact.db")
        try:
            db_connection.execute(funct(*args, **kwargs))
        except:
            print("Cannot Execute statement")
        finally:
            db_connection.close()
            print("Connection closed")
    return db_execute


@connect_db
def create_table():
    statement = '''CREATE TABLE CONTACTS
         (ID INT PRIMARY KEY     NOT NULL,
         FIRSTNAME  TEXT    NOT NULL,
         LASTNAME TEXT NOT NULL,
         PHONENUMBER            CHAR (14)     NOT NULL,
         EMAIL         CHAR (20));'''
    print("Table Created Successfully.")
    return statement
    


@connect_db
def  add_contact():
    first_name = input("Enter the first name.")
    last_name = input("Enter the last name.")
    phone_number = input("Enter the phone number.")
    email = input("Enter the email")

    new_contact = Contact(first_name, last_name, phone_number,email)
    statement = "INSERT INTO CONTACT (ID,FIRSTNAME,LASTNAME,PHONENUMBER,EMAIL) \
      VALUES (1, 'Paul', 'Andrew', '+2349036461479', 'oluwatosindurodola@zohomail.com')"
    print("{} {} has been successfully added".format(new_contact.get_fname(), new_contact.get_lname()))
    return statement


@connect_db
def edit_contact():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email: ")

    new_contact = Contact(first_name, last_name, phone_number,email)
    statement = "UPDATE CONTACT set PHONENUMBER = 25000.00 where PHONENUMBER = PHONENUMBER"
    print("{} {} has been successfully updated".format(new_contact.get_fname(), new_contact.get_lname()))
    return statement


@connect_db
def delete_contact():
    statement = "DELETE from CONTACT where PHONENUMBER = PHONENUMBER"
    print("{} {} has been successfully deleted".format(new_contact.get_fname(), new_contact.get_lname()))
    return statement


def main():
    create_table()
    add_contact()


if __name__ == "__main__":
    main()

