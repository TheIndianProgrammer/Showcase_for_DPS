import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="",
  password="",
  database="main_dev"
)

mycursor = mydb.cursor()

class Program():

    def __init__(self):

        print("==== Initializing School Mangement System... =====")

        print('---------------------------------------------')
        print("         -SCHOOL MANAGEMENT SYSTEM-           ")
        print('---------------------------------------------')

        mycursor.execute("""CREATE TABLE IF NOT EXISTS SCHOOL_MANAGEMENT(NAME TEXT,EMAIL TEXT, PHONE_NO TEXT, GENDER TEXT,STU_STREAM TEXT)""")
        mydb.commit()

    def add_Student(self):
        
        name_str = input("Enter Student name: ")
        email_str = input("Enter Student email: ")
        contact_str = input("Enter Student contact: ")
        gender_str = input("Enter Student gender (Male/Female): ")
        stream_str = input("Enter Student stream: ")

        
        val = [name_str,email_str,contact_str,gender_str,stream_str]
        
        insert_data = ("""
         INSERT INTO SCHOOL_MANAGEMENT(NAME,EMAIL, PHONE_NO, GENDER, STU_STREAM) VALUES(%s, %s, %s, %s, %s)
            """)
        
        mycursor.execute(insert_data, val)
        mydb.commit()

        print('Record added', f"Record of Student:{name_str} was successfully added")
    
    def show_AllRecord(self):
        mycursor.execute("SELECT * FROM SCHOOL_MANAGEMENT")
        Record = mycursor.fetchall()

        print("================All Student Records=================\n")
        print("| Student Name | Email | Phone No | Gender | Stream |")

        for items in Record:
            print("|", items[0], " "*(11-len(items[0])), "|",
                items[1], " "*(4-len(items[1])), "|",
                items[2], " "*(7-len(items[2])), "|",
                items[3], " "*(5-len(items[3])), "|",
                items[4], " "*(5-len(items[4])), "|")
        print("\n")
        print("=====================================================\n")

    def del_Student(self):
        
        del_student = input("Enter Student Name to be deleted: \n")
        mycursor.execute("SELECT * FROM SCHOOL_MANAGEMENT")
        Record = mycursor.fetchall()

        if del_student in Record[0]:
             del_query = ("DELETE FROM SCHOOL_MANAGEMENT WHERE NAME = %s")

             #converting list to a tuple 
             del_student_list = []
             del_student_list.append(del_student)
             del_student_tuple = tuple(del_student_list)

             mycursor.execute(del_query, del_student_tuple)
             mydb.commit()
             print('Record Delted', f"Record of Student:{del_student} was successfully delted")
            
        else:
            print(f"Student:{del_student} was not found!")
    
    def get_Student(self):
        get_student = input("Enter Student Name to be found: \n")
        mycursor.execute("SELECT * FROM SCHOOL_MANAGEMENT")
        Record1 = mycursor.fetchall()

        if get_student in Record1[0]:
             get_query = ("SELECT NAME FROM SCHOOL_MANAGEMENT WHERE NAME = %s")

             #converting list to a tuple 
             get_student_list = []
             get_student_list.append(get_student)
             get_student_tuple = tuple(get_student_list)

             mycursor.execute(get_query, get_student_tuple)
            
             print("================All Student Records=================\n")
             print("| Student Name | Email | Phone No | Gender | Stream |")

             for items in Record1:
                 print("|", items[0], " "*(11-len(items[0])), "|",
                    items[1], " "*(4-len(items[1])), "|",
                    items[2], " "*(7-len(items[2])), "|",
                    items[3], " "*(5-len(items[3])), "|",
                    items[4], " "*(5-len(items[4])), "|")
             print("\n")
             print("=====================================================\n")
            
        else:
            print(f"Student:{get_student} was not found!")




School_Management = Program()

print("======= -Choose an Option: - ======")
print("1: Add a Student")
print("2: Remove a Student")
print("3: Search for a Student")
print("4: Show all students")
print("5: To exit")

while True:
        
    #Input the geometry shape
    choice = int(input("Enter choice:"))

    #Area of circle
    if choice == 1:
        School_Management.add_Student()

    #Area of triangle
    if choice == 2:
        School_Management.del_Student()
        
    #Area of rectangle
    if choice == 3:
        School_Management.get_Student()

    #Area of square
    if choice == 4:
        School_Management.show_AllRecord()

     #To exit
    if choice == 5:
        print("Exiting!")
        break

     #Invalid option entered
    if choice not in (1,2,3,4,5):
        print("Invalid option")