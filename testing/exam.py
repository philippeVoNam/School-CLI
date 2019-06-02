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
from sql_helper import create_connection, create_exam, create_table, delete_exam

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
            'Remove'
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
        'Exit' : exit_
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

    # print(data)

def calendar_() : 
    """ prints out the calendar of the current year """
    print("calendar")

    now = datetime.datetime.now()
    print(calendar.calendar(int(now.year), 2, 1, 1, 4))  

def add() : 
    """ """
    print("add")

    # * Ask user fo the class code and the date of the exams
    questions = [
        {
            'type': 'input',
            'name': 'classCode',
            'message': 'Class Code :',
        },
        {
            'type': 'input',
            'name': 'date',
            'message': 'Date (y/m/d) :'
        },        
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

    answers = prompt(questions, style=custom_style_2)
    classCode = answers['classCode']
    date = answers['date']
    type = answers['type']

    # Find out what is the type and give it a color for it 
    if type == "Assignment" :
        type = colored(type,'white')
    elif type == "Lab Report" :
        type = colored(type,'green')
    elif type == "Midterm" :
        type = colored(type,'yellow')
    elif type == "Final Exam" :
        type = colored(type,'red')

    # Find out how many days left and if less than 5 -> make it bright red
    daysLeft = days_left(parse(date).date())
    if daysLeft < 10 :
        daysLeft = str(daysLeft)
        daysLeft = colored(daysLeft,'white', 'on_red',attrs=['bold'])

    # * Storing the data
    # Connect to a database -> if does not exist -> create
    conn = create_connection("exams_db.sqlite")

    # Execution
    create_table(conn, 'CREATE TABLE IF NOT EXISTS exams (id INTEGER PRIMARY KEY, classCode VARCHAR, type VARCHAR, date VARCHAR, daysLeft VARCHAR, studyTime INTEGER)')
    create_exam(conn,classCode, type, date, daysLeft, 1)

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

# * Logic Functions
def days_left(givenDate) :
    " Returns the number of days between the current date aand the given date "

    currentDate = datetime.datetime.now().date()
    delta = givenDate - currentDate

    return delta.days

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