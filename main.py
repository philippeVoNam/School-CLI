""" 
Author : Philippe Vo
Date : Tue 04 Jun-06 2019 19:55:14
"""
# * IMPORT

# * 3rd Party Library Imports
from termcolor import colored, cprint
from pyfiglet import Figlet, print_figlet, figlet_format
from examples import custom_style_2,custom_style_1
from PyInquirer import style_from_dict, Token, prompt, Separator

# * User Imports
from Exam import Exam
from ExamController import ExamController
from SItemController import SItemController
from Assignment import Assignment

def mode_run(mode) :
    """ Depending on the mode that the user chooses """ 

    switch={'Exams':exam_mode, 'Notes':notes_mode, 'Assignments':assignments_mode} # for some reason I cannot do like the mode_run I did for exam.py ...
    switch[mode]()

def func_run(func, itemClass) :
    """ Depending on the functions that the user chooses """

    controller = SItemController()

    switch={
        'Show':controller.show_table,
        'Add':controller.create_item,
        'Remove':controller.delete_item,
        'Report Numbers Done': controller.modify_numbers_done,
        'View': controller.view_file
        } # for some reason I cannot do like the mode_run I did for exam.py ...
    switch[func](itemClass)

def exam_mode() :
    """ run the exam mode"""

    # Welcome Text("exams_db.sqlite")
    text = "Are you ready for your exams ?"
    cprint(figlet_format(text, font="small"), "green", attrs=['bold'])

    questions = [
    {
        'type': 'list',
        'name': 'mode',
        'message': 'What do you want to do?',
        'choices': [
            Separator(),
            'Show',
            'Calendar',
            'Record Study Time',
            Separator(),
            'Add',
            'Remove',
            'Edit',
            Separator(),
            'Exit'
            ]
        },
    ]

    while True :
        answers = prompt(questions, style=custom_style_2)

        if answers['mode'] == 'Exit' :
            break

        func_run(answers['mode'], Exam)

    print("Done exam operations.")

def notes_mode() : 
    """ run the notes mode """

    # Welcome Text
    text = "Yeah, welcome to the club, pal."
    cprint(figlet_format(text, font="small"), "green", attrs=['bold'])

def assignments_mode() :
    """ run the assignments mode """

    # Welcome Text
    text = "Assignment"
    cprint(figlet_format(text, font="small"), "green", attrs=['bold'])

    questions = [
    {
        'type': 'list',
        'name': 'mode',
        'message': 'What do you want to do?',
        'choices': [
            Separator(),
            'Show',
            'Calendar',
            'Report Numbers Done',
            'View',
            Separator(),
            'Add',
            'Remove',
            'Edit',
            Separator(),
            'Exit'
            ]
        },
    ]

    while True :
        answers = prompt(questions, style=custom_style_2)

        if answers['mode'] == 'Exit' :
            break

        func_run(answers['mode'], Assignment)

    print("Done assignment operations.")



# * Main Function
if __name__ == '__main__' : 

    # Welcome Text
    text = "What is my purpose ? - You take Notes - OH . MY . GOD"
    cprint(figlet_format(text, font="small"), "green", attrs=['bold'])

    question = [
    {
        'type': 'list',
        'name': 'mode',
        'message': 'What do you want to do?',
        'choices': [
            'Homework',
            'Notes',
            'Exams',
            'Assignments',
            'Exit'
            ]
        },
    ]

    # ! Bad design for now -> intentional infinte loop ... 
    exitFlag = False
    while exitFlag != True :
        answers = prompt(question, style=custom_style_2)

        if answers['mode'] == 'Exit' :
            break

        mode_run(answers['mode'])

        cprint(figlet_format(text, font="small"), "green", attrs=['bold'])
    
    print("exiting program.")