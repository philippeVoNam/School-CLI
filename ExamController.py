"""
Author : Philippe Vo
Date : Tue 04 Jun-06 2019 19:17:37
"""

# * IMPORTS
# * imports for the PyInquirer
from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_2,custom_style_1
# * imports for the PyInquirer

# * 3rd Library Imports
from pyfiglet import Figlet, print_figlet, figlet_format
from terminaltables import AsciiTable
import click
import calendar 
import datetime
import sqlite3
import sys
from datetime import date
from dateutil.parser import parse
from termcolor import colored, cprint
from colorama import init
init(strip=not sys.stdout.isatty())
from blessings import Terminal


# * USER IMPORTS
from sql_helper import create_connection, create_exam, create_table, delete_exam, update_exam, create_connection_db
from StopWatch import stopwatch
from SItemController import SItemController
from Exam import Exam

class ExamController:
    """
    controller to add / remove / edit / create 
    exams from the database

    Attributes 
    ----------
    - database file

    Methods
    ------- 
    - add ( ) 
        - lets the user add an exam to the database
    - remove ( Grid )
        - lets the user remove an exam from the database
    - edit ( )
        - lets the user edit an exam from the database
    - input_exam ( )
        - calls al the helper functions to make an exam 

    Logic Functions
    ---------------
    - days_left ( )
        - calculates the number of days left, given the date and the current date
    - date_validation ( )
        - validates if the date is valid or not
    
    Helper Functions
    ----------------
    - date_input ( )
        - ask user for date input
    - type_input ( )
        - ask user for type input
    - classCode_input ( )
        - ask user for classCode input 

    """

    def __init__(self, database) :
        """ construcor """

        # Init the database
        self.database = database

    def mode_run(self, mode) : 
        """ Depending on the mode that the user chooses """ 
        
        modes = {
            'Show' : self.show,
            'Calendar' : self.calendar_,
            'Record Study Time' : self.record_study_time, 
            'Add'  : self.add,
            'Remove' : self.remove,
            'Exit' : self.exit_,
            'Edit' : self.edit
            }

        func = modes.get(mode)
        func()

    def exit_(self) :
        """ Terminates the current School-CLI session """

        return True

    def show(self) : 
        """ """
        print("show")

        # Fetch all the exams from the database
        conn = create_connection(self.database)
        cur = conn.cursor()
        cur.execute('SELECT * FROM exams')
        data = cur.fetchall()

        tableData = [
        ['id','Class Code','Type', 'Date', 'Days Left', 'Study Time']
        ]

        for exam in data : 
            
            tableData.append(exam)

        table = AsciiTable(tableData)
        print (table.table)

    def calendar_(self) : 
        """ prints out the calendar of the current year """
        print("calendar")

        now = datetime.datetime.now()
        print(calendar.calendar(int(now.year), 2, 1, 1, 4))  

    def add(self) : 
        """ """
        # print("add")

        # # * Get the information about the exam the user input
        # info = self.input_exam()

        # classCode = info["classCode"]
        # type = info["type"]
        # date = info["date"]
        # daysLeft = info["daysLeft"]
        # studyTime = info["studyTime"]

        # # * Storing the data
        # # Connect to a database -> if does not exist -> create
        # conn = create_connection(self.database)

        # # Execution
        # create_table(conn, 'CREATE TABLE IF NOT EXISTS exams (id INTEGER PRIMARY KEY, classCode VARCHAR, type VARCHAR, date VARCHAR, daysLeft VARCHAR, studyTime VARCHAR)')
        # create_exam(conn,classCode, type, date, daysLeft, studyTime)

        # # Saves the changes you made and quit
        # conn.commit()
        # conn.close()

        controller = SItemController()

        # * Adding to the database
        # Connecting to the database
        # conn = create_connection_db(Exam)

        controller.create_item_db(Exam)

    def remove(self) : 
        """ """
        print("remove")

        # Show the exams available
        self.mode_run("Show")

        # * Ask user fo the class code and the date of the exams
        id = self.id_input()

        # Confirmation question
        confirmation = [
            {
                'type': 'confirm',
                'message': 'Are you sure you want to remove exam ?',
                'name': 'confirm',
                'default': False,
            }
        ]

        confirmation_answer = prompt(confirmation, style=custom_style_1)

        if confirmation_answer['confirm'] == True :
            # Connect to a database -> if does not exist -> create
            conn = create_connection(self.database)

            # Delete the exam with given id
            delete_exam(conn, id)

            # Saves the changes you made and quit
            conn.commit()
            conn.close()

        else :
            print("Operation Canceled.")

    def edit(self) :
        """ edit an exam that was already entered """
        print("edit")

        # Show the exams available
        self.mode_run("Show")

        # * Ask user fo the id
        id = self.id_input()

        # Confirmation question
        confirmation = [
            {
                'type': 'confirm',
                'message': 'Are you sure you want to edit exam ?',
                'name': 'confirm',
                'default': False,
            }
        ]

        confirmationAnswer = prompt(confirmation, style=custom_style_1)

        if confirmationAnswer['confirm'] == True :
            # Connect to a database -> if does not exist -> create
            conn = create_connection(self.database)

            # * Edit the exam with given id
            editQuestion = [
                {
                    'type': 'list',
                    'name': 'item',
                    'message': 'Which item would you like to edit ?',
                    'choices': [
                        'Class Code',
                        'Type',
                        'Date',
                        'Quit'
                        ]
                    },
                ]       

            cur = conn.cursor()
            cur.execute("SELECT * FROM exams WHERE id=?", (id,))
            data = cur.fetchall()

            # Saving the data for delivery
            id = data[0][0]
            classCode = data[0][1]
            type = data[0][2]
            date = data[0][3]
            daysLeft = data[0][4]
            studyTime = data[0][5]

            # Editing the specific data the user wants to edit
            quitFlag = False
            while quitFlag != True :
                editQuestionAnswer = prompt(editQuself.id - idestion, style=custom_style_2)
                
                if editQuestionAnswer['item'] == 'Quit' :
                    quitFlag = True
                    
                    # Saves the changes you made and quit
                    conn.commit()
                    conn.close()
                    return

                if editQuestionAnswer['item'] == 'Type' :
                    type = self.type_input()

                elif editQuestionAnswer['item'] == 'Date' :
                    date = self.date_input()

                    # Find out how many days left and if less than 5 -> make it bright red
                    daysLeft = self.days_left(parse(date).date())
                    if daysLeft < 10 :
                        daysLeft = str(daysLeft)
                        daysLeft = colored(daysLeft,'white', 'on_red',attrs=['bold'])
                    else :
                        daysLeft = str(daysLeft)

                else :
                    classCode = self.classCode_input()

                # Update
                update_exam(conn, id, classCode, type, date, daysLeft, studyTime)

        else :
            print("Operation Canceled.")

    def input_exam(self) :
        """ ask user for input on exam info """

        # * Ask user fo the class code and the date of the exams
        classCode = self.classCode_input()
        date = self.date_input()
        type = self.type_input()

        # Find out how many days left and if less than 5 -> make it bright red
        daysLeft = self.days_left(parse(date).date())
        if daysLeft < 10 :
            daysLeft = str(daysLeft)
            daysLeft = colored(daysLeft,'white', 'on_red',attrs=['bold'])
        else :
            daysLeft = str(daysLeft)

        info = {
            "classCode": classCode,
            "type": type,
            "date": date,
            "daysLeft": daysLeft,
            "studyTime": '00:00:05'
        }

        return info

    def record_study_time(self) :
        """ starts a stopwatch and records the time, when the users stop it -> appends the time to the exam """

        # Show the exams available
        self.mode_run("Show")

        # Ask the user for the exam they want to record tihe study time
        id = self.id_input()

        # Start the stopwatch        
        currentTime = stopwatch()
        currentTime = datetime.timedelta(seconds=round(currentTime)) # convert float to time obj

        # Retrieve the study time of the given id 
        conn = create_connection(self.database)
        cur = conn.cursor()
        sql = ''' SELECT studyTime FROM exams WHERE id=? '''
        cur.execute(sql, (id,))
        data = cur.fetchone()

        # Constructing the datetime.time obj from string
        retrievedTime = datetime.datetime.strptime(data[0], '%H:%M:%S').time()
        retrievedTime = datetime.timedelta(hours=retrievedTime.hour, minutes=retrievedTime.minute, seconds=retrievedTime.second) # converting the time to timedelta
        
        # Appending the time 
        totalTime = str((currentTime + retrievedTime))

        # Updating the database
        sql = ''' UPDATE exams
              SET 
                    studyTime = ?
              WHERE 
                    id = ?'''
        cur.execute(sql, (totalTime,id))

        # Closing the database
        conn.commit()
        conn.close()

    # * Logic Functions
    def days_left(self, givenDate) :
        " Returns the number of days between the current date aand the given date "

        currentDate = datetime.datetime.now().date()
        delta = givenDate - currentDate

        return delta.days
    # Input + add_db

    def date_validation(self, dateStr) : 
        """ checks if the date is valid """

        try:
            parse(dateStr).date()
            return True
        except ValueError as e:
            print(e)

        return False

    # * Helper Functions
    def date_input(self) :
        """ ask the user for the date """
        
        # Date Validation
        dateQuestion = [
                {
                    'type': 'input',
                    'name': 'date',
                    'message': 'Date (y/m/d) :'
                }
        ]
        answersDate = prompt(dateQuestion, style=custom_style_2)
        date = answersDate['date']
        while self.date_validation(answersDate['date']) == False : 
                answersDate = prompt(dateQuestion, style=custom_style_2)
                date = answersDate['date']

        return date

    def type_input(self) :
        """ ask the user for the type """
        typeQuestion = [  
            {
                'type': 'list',
                'name': 'type',
                'message': 'Type ?',
                'choices': [
                    'Assignment',
                    'Lab Report',
                    'Midterm',
                    'Final Exam'
                    ]
            }
        ]

        typeQuestionAnswer = prompt(typeQuestion, style=custom_style_2)
        type = typeQuestionAnswer['type']
                        
        # Find out what is the type and give it a color for it 
        if type == "Assignment" :
            type = colored(type,'white')
        elif type == "Lab Report" :
            type = colored(type,'green')
        elif type == "Midterm" :
            type = colored(type,'yellow')
        elif type == "Final Exam" :
            type = colored(type,'red')

        return type

    def classCode_input(self) :
        """ ask the user for the classCode """
        
        # * Ask user fo the class code and the date of the exams
        classCodeQuestion = [
            {
                'type': 'input',
                'name': 'classCode',
                'message': 'Class Code :',
            }
        ]

        classCodeQuestionAnswer = prompt(classCodeQuestion, style=custom_style_2)
        classCode = classCodeQuestionAnswer['classCode']

        return classCode 

    def id_input(self) :
        """ ask the user for the id """

        # * Ask user fo the id
        questions = [
            {
                'type': 'input',
                'name': 'id',
                'message': 'id :',
            }
        ]

        answers = prompt(questions, style=custom_style_2)
        id = answers['id']

        return id

# # * Main Function
# if __name__ == '__main__' : 

#     controller = ExamController("exams_db.sqlite")

#     # Welcome Text
#     text="Are you ready for your exams ?"
#     cprint(figlet_format(text, font="small"), "green", attrs=['bold']) 

#     questions = [
#     {
#         'type': 'list',
#         'name': 'mode',
#         'message': 'What do you want to do?',
#         'choices': [
#             Separator(),
#             'Show',
#             'Calendar',
#             Separator(),
#             'Add',
#             'Remove',
#             'Edit',
#             Separator(),
#             'Exit'
#             ]
#         },
#     ]

#     # ! Bad design for now -> intentional infinte loop ... 
#     while (True) :
#         answers = prompt(questions, style=custom_style_2)
#         controller.mode_run(answers['mode'])