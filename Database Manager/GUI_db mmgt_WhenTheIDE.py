import sqlite3                    #importing module for performing SQL operations.
from tkinter import *             #importing module for creating GUI
from tkinter import messagebox


#===============================================================================================

class DB:                         #creating a class DB with functions to perform various operations on the database. 
    def __init__(self):           #constructor functor for class DB.
        self.conn = sqlite3.connect("C:\Programming\_Projects\Web Devolopment\WhenTheIDE\Database\database.sqlite")  #connects to a database called mytwitch_datas.db
        self.cur = self.conn.cursor()    #creating a cursor to navigate through the database
        self.cur.execute('''CREATE TABLE IF NOT EXISTS twitch_data(
                            id INTEGER PRIMARY KEY,
                            Streamer_name char(1000),
                            Streamer_raw_link char(1000),
                            IDE_name char(1000),
                            IDE_raw_link char(1000))
                            ''')
        self.conn.commit()  #commit functions saves everything to the database

    def __del__(self):          #destructor created for the class DB
        self.conn.close()   #closes the connection with the database

    def view(self):         #To view all the rows present in the table
        self.cur.execute("SELECT * FROM twitch_data") #Execute function is to perform the SQL operations. Here, it produces all the rows from the table.
        rows = self.cur.fetchall()  #fetching all the rows one by one from the table and storing it in list rows
        return rows

    def insert(self, Streamer_name, Streamer_raw_link, IDE_name, IDE_raw_link,):  #inserting a new row in the table. 
        self.cur.execute("INSERT INTO twitch_data VALUES (NULL,?,?,?,?)", (Streamer_name, Streamer_raw_link, IDE_name,IDE_raw_link,)) #passing values to the function to store them in the columns
        self.conn.commit()
        self.view()

    def update(self, id, Streamer_name, Streamer_raw_link):    #to update the values of the selected row with the values passed by the user
        self.cur.execute("UPDATE twitch_data SET Streamer_name=?, Streamer_raw_link=? WHERE id=?", (Streamer_name, Streamer_raw_link, id,))
        self.conn.commit()
        self.view()

    def delete(self, id):                   #to delete the row from the table given the value of the id of the selected row.
        self.cur.execute("DELETE FROM twitch_data WHERE id=?", (id,))
        self.conn.commit()
        self.view()

    def search(self, Streamer_name="", Streamer_raw_link=""):  #to search for a given entry in the table given either the value of the Streamer_name or Streamer_raw_link name
        self.cur.execute("SELECT * FROM twitch_data WHERE Streamer_name=? OR Streamer_raw_link=?", (Streamer_name, Streamer_raw_link,))
        rows = self.cur.fetchall()
        return rows

db = DB()

#=============================================================================================

def get_selected_row(event): #selecting a particular row or multiple rows
    global selected_tuple
    index = list1.curselection()[0] #this is the id of the selected tuple
    selected_tuple = list1.get(index) 

    e1.delete(0, END)                 #deleting the value so that can be used again for next twitch_data
    e1.insert(END, selected_tuple[1]) #inserting the title of the twitch_data

    e2.delete(0, END)
    e2.insert(END, selected_tuple[2]) #inserting author name

    e3.delete(0, END)
    e3.insert(END, selected_tuple[3]) #IDE_name

    e4.delete(0, END)
    e4.insert(END, selected_tuple[4]) #IDE_raw_link

def view_command():         #to print all the rows of the table using view function of the class DB on to the screen 
    list1.delete(0, END)    #empty the list
    for row in db.view():   #loop until we reach the end of the table twitch_data
        list1.insert(END, row)

def search_command():       #to print the row we want based on title or author 
    list1.delete(0, END)    #empty the list
    for row in db.search(Streamer_name_text.get(), Streamer_raw_link_text.get()): #get the name of the title or the author and pass it to the search function of class DB
        list1.insert(END, row)

def add_command():          #to add a new row into the table
    db.insert(Streamer_name_text.get(), Streamer_raw_link_text.get(), IDE_name_text.get(), IDE_raw_link_text.get()) #passing user input values 
    list1.delete(0, END) #empty the list
    list1.insert(END, (Streamer_name_text.get(), Streamer_raw_link_text.get(), IDE_name_text.get(), IDE_raw_link_text.get()))

def delete_command(): #deleting a row 
    db.delete(selected_tuple[0])

def update_command():
    db.update(selected_tuple[0], Streamer_name_text.get(), Streamer_raw_link_text.get())

window = Tk() #using Tkinter module, create a GUI window

window.title("My twitch_data") #setting title of the window


def on_closing(): #destructor for the window
    dd = db
    if messagebox.askokcancel("Quit", "Do you want to quit?"): #when ok is clicked, displays the following message
        window.destroy()
        del dd #deletes the object once window has been closed

window.protocol("WM_DELETE_WINDOW", on_closing)


l1 = Label(window, text="Streamer_name") #creating input labels in the window
l1.grid(row=0, column=0) #determining size of the input grid for these labels

l2 = Label(window, text="Streamer_raw_link")
l2.grid(row=0, column=2)

l3 = Label(window, text="IDE_name")
l3.grid(row=1, column=0)

l4 = Label(window, text="IDE_link")
l4.grid(row=1, column=2)

#title_text
Streamer_name_text = StringVar()
e1 = Entry(window, textvariable=Streamer_name_text) #taking input from the user in the grid and storing it in a string variable
e1.grid(row=0, column=1)

#Streamer_raw_link_text
Streamer_raw_link_text = StringVar() #taking author name input
e2 = Entry(window, textvariable=Streamer_raw_link_text)
e2.grid(row=0, column=3)

#IDE_name_text
IDE_name_text = StringVar() #taking isbn input
e3 = Entry(window, textvariable=IDE_name_text)
e3.grid(row=1, column=1)

#e4
IDE_raw_link_text = StringVar() #taking isbn input
e4 = Entry(window, textvariable=IDE_raw_link_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=25, width=65) #creating the list space to display all the rows of the table
list1.grid(row=2, column=0, rowspan=6, columnspan=2) #determining the size

sb1 = Scrollbar(window) #creating a scrollbar for the window to scroll through the list entries
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set) #configuring the scroll function for the scrollbar object sb1
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command) #creating buttons for the various operations. Giving it a name and assigning a particular command to it. 
b1.grid(row=2, column=3) #size of the button

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()