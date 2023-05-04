import psycopg2
import csv

conn = psycopg2.connect(database="postgres", user="postgres", password="1234", host="localhost", port="5432")

def add_contact(name, phone_number):
    cur = conn.cursor()  
    cur.execute("INSERT INTO phonebook (name, phone_number) VALUES (%s, %s)", (name, phone_number))
    conn.commit()
    cur.close()

def update_contact(id, name, phone_number):
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET name=%s, phone_number=%s WHERE id=%s", (name, phone_number,id))
    conn.commit()
    cur.close()

def delete_contact(name):
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()
    cur.close()

def get_phonebook():
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    cur.close()
    return rows

def get_contact(id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE id=%s", (id,))
    row = cur.fetchone()
    cur.close()
    return row

def get_phonebook_by_name(name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    rows = cur.fetchall()
    cur.close()
    return rows

def get_contact_by_character(char):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name LIKE %s", ('%'+char+'%',))
    rows = cur.fetchall()
    cur.close()
    return rows

def get_phonebook_with_phone_number( digits):
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE phone_number LIKE %s", ('%' + digits + '%',))
    rows = cur.fetchall()
    cur.close()
    return rows
def call_insert_user(name, phone):
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_contact(%s, %s)", (name, phone))
    conn.commit()
    cur.close()

def call_insert_users():
    cur = conn.cursor()
    # ask the user to enter a list of sub-lists
    input_str = input("Enter a list of sub-lists in the format [['name1', 'number1'], ['name2', 'number2'], ...]: ")
    # evaluate the input string as a Python expression to get the list of sub-lists
    phonebook_list = eval(input_str)
    phonebook_array = psycopg2.extensions.adapt(phonebook_list).getquoted().decode()
    sql = f"CALL insert_multiple_phonebook({phonebook_array})"

    cur.execute(sql)
    conn.commit()
    cur.close()

def get_data_with_pagination(table_name, limit, offset):
    cur = conn.cursor()
    # execute SQL query
    query = "SELECT * FROM {} LIMIT %s OFFSET %s".format(table_name)
    cur.execute(query, (limit, offset))
    # fetch rows
    rows = cur.fetchall()
    conn.close()
    return rows

def delete():
    cur = conn.cursor()
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    cur.execute("CALL delete_data(%s, %s)", (name, phone_number))
    conn.commit()
    cur.close()

while True:
    command = input("which one?(add,csv,update,delete,get_all,get_one,get_name,get_phone_number,get_name_with_c,exit,pro,multiple_phonebook,query,dele):")
    if command == "add":
        name = input("please enter the name:")
        phone_number = input("please enter the phone number:")
        add_contact(name, phone_number)
    elif command == "csv":
        with open('phonebook.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader) 
            for row in reader:
                try:
                    name = row[0]
                    phone_number = row[1]
                    add_contact(name, phone_number)
                except (IndexError, ValueError) as e:
                    print(f"Coundn't add... {row}: {e}")
    elif command == "update":
        id = input("please enter the ID:")
        name = input("please enter the name:")
        phone_number = input("please enter the phone number:")
        update_contact(id, name, phone_number)
    elif command == "delete":
        n = input("please enter the name:")
        delete_contact(n)
    elif command == "get_all":
        phonebook = get_phonebook()
        for contact in phonebook:
            print(contact)
    elif command == "get_one":
        id = input("please enter contact's id:")
        contact = get_contact(id)
        print(contact)
    elif command == "get_name":
        name = input("please enter name:")
        names = get_phonebook_by_name(name)
        print(names)
    elif command == "get_phone_number":
        pn = input("please enter digit:")
        pns = get_phonebook_with_phone_number(pn)
        print(pns)
    elif command == "get_name_with_c":
        c = input("please enter character:")
        cs = get_contact_by_character(c)
        print(cs)
    elif command == "pro":
        namee = input("please enter your name:")
        phonen = input("please enter your phone number:")
        call_insert_user(namee,phonen)
    elif command == "multiple_phonebook":
        call_insert_users()
    elif command == "query":
        data = get_data_with_pagination("phonebook", 10, 0)
        print(data)
    elif command == "dele":
        delete()
    elif command == "exit":
        break
    else:
        print("error execution...")

conn.close()