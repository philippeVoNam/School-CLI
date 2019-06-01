""" 
Author : Philippe Vo
Date : Sat 01 Jun-06 2019 15:11:23
"""

# * IMPORTS

# * imports for the PyInquirer
from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_2
# * imports for the PyInquirer

# * 3rd Library Imports
from pyfiglet import Figlet
from pyfiglet import print_figlet
import click
import calendar 
import datetime
import sqlite3
from terminaltables import AsciiTable

# * USER IMPORTS

from sql_helper import create_connection, create_exam, create_table

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
        'Remove' : remove
        }

    func = modes.get(mode)
    func()

def show() : 
    """ """
    print("show")

    # Fetch all the exams from the database
    conn = create_connection("exams_db.sqlite")
    cur = conn.cursor()
    cur.execute('SELECT * FROM exams')
    data = cur.fetchall()

    tableData = [
    ['Class Code', 'Date']
    ]

    for exams in data : 
        tableData.append(exams)

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
        }
    ]

    answers = prompt(questions, style=custom_style_2)
    classCode = answers['classCode']
    date = answers['date']


    # * Storing the data
    # Connect to a database -> if does not exist -> create
    conn = create_connection("exams_db.sqlite")

    # Execution
    create_table(conn, 'CREATE TABLE IF NOT EXISTS exams (classCode VARCHAR, date VARCHAR)')
    create_exam(conn,classCode, date)

    # Saves the changes you made and quit
    conn.commit()
    conn.close()

def remove() : 
    """ """
    print("remove")

    click.secho('Hello World!', fg='green')
    click.secho('Some more text', bg='blue', fg='white')
    click.secho('ATTENTION', blink=True, bold=True)

if __name__ == '__main__' : 
    mode = main()
    # print(type(mode))
    # print("Done.")
    



