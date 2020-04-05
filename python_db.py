import sqlite3
from tkinter import *
from PIL import ImageTk, Image
from sqlite3 import *

root = Tk()
root.geometry("400x400")
root.title("DATABASE")
# database

# create a database or connect to one
con = sqlite3.connect('addressbook.db')
# cursor is used to send with instruction and return with one
# create cursor
c = con.cursor()
# create table
'''
c.execute("""CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer)""")

'''


# create submit function
def submit():
    con = sqlite3.connect('addressbook.db')
    c = con.cursor()

    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': fname.get(),
                  'l_name': lname.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })
    # commit changes
    con.commit()

    # close connection
    con.close()
    fname.delete(0, END)
    lname.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)



def query():
    global records
    con = sqlite3.connect('addressbook.db')
    c = con.cursor()

    c.execute("SELECT *, oid FROM addresses") # by default sqlite 3 gives the oid but ignores it
    records = c.fetchall()
    # print(records)
    print_records = ''
    for record in records:
        print_records += str(record[0])+" "+ str(record[1])+ " "+ str(record[6])+" " +"\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)
    # commit changes
    con.commit()

    # close connection
    con.close()

def delete():
    con = sqlite3.connect('addressbook.db')
    c = con.cursor()
    c.execute("DELETE FROM addresses WHERE oid = "+ delete_widget.get())

    con.commit()
    con.close()

# create a function to update the records in new window
def update():
    con = sqlite3.connect('addressbook.db')
    c = con.cursor()
    record_id=delete_widget.get()
    c.execute("""UPDATE addresses SET
        first_name= :first,
        last_name=:last,
        address=:address,
        city= :city,
        state =:state,
        zipcode=:zipcode
        
        WHERE oid=:oid""",
              {
                  'first':fname_editor.get(),
                  'last':lname_editor.get(),
                  'address':address_editor.get(),
                  'city':city_editor.get(),
                  'state':state_editor.get(),
                  'zipcode':zipcode_editor.get(),

                  'oid': record_id
              })
    con.commit()
    con.close()
    editor.destroy()





# create a function to edit the records
def edit():
    global editor
    editor = Tk()
    editor.geometry("400x400")
    editor.title("UPDATE A RECORD")
    con = sqlite3.connect('addressbook.db')
    c = con.cursor()

    record_id = delete_widget.get()
    c.execute("SELECT * FROM addresses WHERE oid= " + record_id)  # by default sqlite 3 gives the oid but ignores it
    records = c.fetchall()
    # print(records)
    # loop through results
    global fname_editor,lname_editor, address_editor, city_editor, state_editor, zipcode_editor
    fname_editor = Entry(editor, width=30)
    fname_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    lname_editor = Entry(editor, width=30)
    lname_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)


    # create labels
    fnamelabel = Label(editor, text="First name")
    fnamelabel.grid(row=0, column=0, padx=20, pady=(10, 0))
    lnamelabel = Label(editor, text="Last name")
    lnamelabel.grid(row=1, column=0)
    addresslabel = Label(editor, text="Address")
    addresslabel.grid(row=2, column=0)
    citylabel = Label(editor, text="City")
    citylabel.grid(row=3, column=0)
    statelabel = Label(editor, text="State")
    statelabel.grid(row=4, column=0)
    zipcodelabel = Label(editor, text="Zipcode")
    zipcodelabel.grid(row=5, column=0)

    for record in records:
        fname_editor.insert(0, record[0])
        lname_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])


    save_button = Button(editor, text="SAVE RECORDS", command=update)
    save_button.grid(row=6, column=0, columnspan=2)

    # commit changes
    con.commit()

    # close connection
    con.close()






# create text boxes
fname = Entry(root, width=30)
fname.grid(row=0, column=1, padx=20, pady=(10,0))
lname = Entry(root, width=30)
lname.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
# create a delete entry widget
delete_widget = Entry(root, width=30)
delete_widget.grid(row=9, column=1)

# create labels
fnamelabel = Label(root, text="First name")
fnamelabel.grid(row=0, column=0, padx=20, pady=(10,0))
lnamelabel = Label(root, text="Last name")
lnamelabel.grid(row=1, column=0)
addresslabel = Label(root, text="Address")
addresslabel.grid(row=2, column=0)
citylabel = Label(root, text="City")
citylabel.grid(row=3, column=0)
statelabel = Label(root, text="State")
statelabel.grid(row=4, column=0)
zipcodelabel = Label(root, text="Zipcode")
zipcodelabel.grid(row=5, column=0)
delete_label=Label(root, text="Select ID")
delete_label.grid(row=9, column=0)

# create submit button
submit_button = Button(root, text="SUBMIT", command=submit)
submit_button.grid(row=6, column=0, columnspan=2)
query_button = Button(root, text="SHOW RECORDS", command=query)
query_button.grid(row=7, column=0, columnspan=2)
delete_button= Button(root, text="DELETE RECORDS", command=delete)
delete_button.grid(row=10, column=0, columnspan=2)
edit_button= Button(root, text="EDIT RECORDS", command=edit)
edit_button.grid(row=11, column=0, columnspan=2)

# commit changes
con.commit()

# close connection
con.close()

root.mainloop()
