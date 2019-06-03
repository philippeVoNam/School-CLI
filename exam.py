""" 
Author : Philippe Vo
Date : Sat 01 Jun-06 2019 15:11:23
"""

# * IMPORTS
# * imports for the PyInquirer
from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_2,custom_style_1
# * imports for the PyInquirer

# * 3rd Library Imports
from pyfiglet import Figlet
from pyfiglet import print_figlet
import click
import calendar 
import datetime
import sqlite3
import sys
from terminaltables import AsciiTable
from datetime import date
from dateutil.parser import parse
from termcolor import colored

# * USER IMPORTS
from sql_helper import create_connection, create_exam, create_table, delete_exam, update_exam

# CODE 

@click.command()
# @click.option('--exam')
def main() : 
    # f = Figlet(font='small',)
    # print(f.renderText('Are you ready for your exams ?'))

    questions = [
    {
        'type': 'list',
        'name': 'mode',
        'message': 'What do you want to do?',
        'choices': [
            Separator(),
            'Show',
            'Calendar',
            Separator(),
            'Add',
            'Remove',
            'Edit'
            ]
        },
    ]

    answers = prompt(questions, style=custom_style_2)
    mode_run(answers['mode'])

    return answers 

def mode_run(mode) : 
    """ Depending on the mode that the user chooses """ 
    
    modes = {
        'Show' : show,
        'Calendar' : calendar_,
        'Add'  : add,
        'Remove' : remove,
        'Exit' : exit_,
        'Edit' : edit
        }

    func = modes.get(mode)
    func()

def exit_() :
    """ Terminates the current School-CLI session """

    sys.exit(0)

def show() : 
    """ """
    print("show")

    # Fetch all the exams from the database
    conn = create_connection("exams_db.sqlite")
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

def calendar_() : 
    """ prints out the calendar of the current year """
    print("calendar")

    now = datetime.datetime.now()
    print(calendar.calendar(int(now.year), 2, 1, 1, 4))  

def add() : 
    """ """
    print("add")

    # * Get the information about the exam the user input
    info = input_exam()

    classCode = info["classCode"]
    type = info["type"]
    date = info["date"]
    daysLeft = info["daysLeft"]
    studyTime = info["studyTime"]

    # * Storing the data
    # Connect to a database -> if does not exist -> create
    conn = create_connection("exams_db.sqlite")

    # Execution
    create_table(conn, 'CREATE TABLE IF NOT EXISTS exams (id INTEGER PRIMARY KEY, classCode VARCHAR, type VARCHAR, date VARCHAR, daysLeft VARCHAR, studyTime INTEGER)')
    create_exam(conn,classCode, type, date, daysLeft, studyTime)

    # Saves the changes you made and quit
    conn.commit()
    conn.close()

def remove() : 
    """ """
    print("remove")

    # Show the exams available
    mode_run("Show")

    # * Ask user fo the class code and the date of the exams
    questions = [
        {
            'type': 'input',
            'name': 'id',
            'message': 'id :',
        }
    ]

    answers = prompt(questions, style=custom_style_2)
    id = answers['id']

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
        conn = create_connection("exams_db.sqlite")

        # Delete the exam with given id
        delete_exam(conn, id)

        # Saves the changes you made and quit
        conn.commit()
        conn.close()
    else :
        print("Operation Canceled.")

def edit() :
    """ edit an exam that was already entered """
    print("edit")

    # Show the exams available
    mode_run("Show")

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
        conn = create_connection("exams_db.sqlite")

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
            editQuestionAnswer = prompt(editQuestion, style=custom_style_2)
            
            if editQuestionAnswer['item'] == 'Quit' :
                quitFlag = True
                
                # Saves the changes you made and quit
                conn.commit()
                conn.close()
                return

            if editQuestionAnswer['item'] == 'Type' :
                type = type_input()

            elif editQuestionAnswer['item'] == 'Date' :
                date = date_input()

                # Find out how many days left and if less than 5 -> make it bright red
                daysLeft = days_left(parse(date).date())
                if daysLeft < 10 :
                    daysLeft = str(daysLeft)
                    daysLeft = colored(daysLeft,'white', 'on_red',attrs=['bold'])
                else :
                    daysLeft = str(daysLeft)

            else :
                classCode = classCode_input()

            # Update
            update_exam(conn, id, classCode, type, date, daysLeft, studyTime)

    else :
        print("Operation Canceled.")

def input_exam() :
    """ ask user for input on exam info """

    # * Ask user fo the class code and the date of the exams
    classCode = classCode_input()
    date = date_input()
    type = type_input()

    # Find out how many days left and if less than 5 -> make it bright red
    daysLeft = days_left(parse(date).date())
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
        "studyTime": 1
    }

    return info

# * Logic Functions
def days_left(givenDate) :
    " Returns the number of days between the current date aand the given date "

    currentDate = datetime.datetime.now().date()
    delta = givenDate - currentDate

    return delta.days

def date_validation(dateStr) : 
    """ checks if the date is valid """

    try:
        parse(dateStr).date()
        return True
    except ValueError as e:
        print(e)

    return False

# * Helper Functions

def date_input() :
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
    while date_validation(answersDate['date']) == False : 
            answersDate = prompt(dateQuestion, style=custom_style_2)
            date = answersDate['date']

    return date

def type_input() :
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

def classCode_input() :
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

# * Main Function
if __name__ == '__main__' : 

    questions = [
    {
        'type': 'list',
        'name': 'mode',
        'message': 'What do you want to do?',
        'choices': [
            Separator(),
            'Show',
            'Calendar',
            Separator(),
            'Add',
            'Remove',
            'Edit',
            Separator(),
            'Exit'
            ]
        },
    ]

    # ! Bad design for now -> intentional infinte loop ... 
    while (True) :
        answers = prompt(questions, style=custom_style_2)
        mode_run(answers['mode'])
    
# date = date(2019,5,20)
# days_left(date)

# date = parse('2018-06-29').date()
# # print(datetime.date())  
# print(days_left(date))

# gin