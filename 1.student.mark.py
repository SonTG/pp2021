from typing import Optional


student = []
course = []
mark = []

def Information():
    print("--------------------------------")
    print()

    # Input Student information ##############################
    # Contain:
    #     - ID
    #     - Name
    #     - Date of Birth

    s_Num = int(input("How many students?\n  -> There are: "))
    while (s_Num == None):    

        s_Num = int(input("Try again?\n  -> There are: "))
        if (s_Num != None):
            break
    for i in range(s_Num):
        print("    * Enter information about student " + str(i + 1) + ": ")
        s_ID = input("      - Student " + str(i + 1) + " ID: ")
        s_Name = input("      - Student " + str(i + 1) + " Name: ")
        s_DoB = input("      - Student " + str(i + 1) + " DoB: ")
        student.append({"Student Id": s_ID, "Student Name": s_Name, "Student DoB": s_DoB})
        print()

    # Input Course information ###############################
    # Contain:
    #      - ID
    #      - Name

    c_Num = int(input("How many courses?\n  -> There are: "))
    for i in range(c_Num):
        print("    * Enter information about course " + str(i + 1) + ": ")
        c_ID = input("      - Course " + str(i + 1) +" ID: ")
        c_Name = input("      - Course " + str(i + 1) +" Name: ")
        course.append({"Course Id": c_ID, "Course Name": c_Name})
        print()
        print("-----------------------------------------------------------------")

# Show
###
def show_Student():
    print(" # Information about students:")
    print(student)
    print()

def show_Course():
    print(" # Information about courses:")
    print(course)
    print()
    
###

def mark_Course():
    print("-------------------------------")
    print()

    # Input for choosing:
    #      - Student:      ###########################
    show_Student()
    print(" => Select student by ID:")
    s_ID = input("    +> Option: ")
    print("--------------------------------------------------------")

    #      - Course:       ###########################
    show_Course()
    print(" => Select course by ID:")
    c_ID = input("    +> Option: ")
    print("--------------------------------------------------------")

    # Mark #######################################
    print()
    m = input(" => Enter the mark: ")
    mark.append({"Student ID": s_ID, "Course ID": c_ID, "Mark": m})
    print()

def show_Marks():
    print(" Here is the list of mark")
    print(mark)
    print()

def option():
    # Option: ########################################
    answer = ""
    while (True):
        print("Select an option below: ")
        print("    +> 1. Input information about student and course")
        print("    +> 2. Input mark of student and course")
        print("    +> 3. Show information about student")
        print("    +> 4. Show information about course")
        print("    +> 5. Show mark of students in courses")
        print("""
         If you find that this program is to bad, just follow the step below.
         Have fun!!
         :)""")
        print("    +> 0. Type '0' ('zero') to quit")

        choose = input("      => Your option: ")
        if (choose == "1"):
            Information()
        if (choose == "2"):
            mark_Course()
        if (choose == "3"):
            show_Student()
        if (choose == "4"):
            show_Course()
        if (choose == "5"):
            show_Marks()
        if (choose == "0"):
            break
    print("""  :)
        Thanks for using this.
        See you later.
        Have fun!
        :)""")

# Information()
# # show_Student()
# # show_Course()
# mark_Course()
# show_Marks()
option()