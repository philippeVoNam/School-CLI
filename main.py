""" 
Author : Philippe Vo
Date : Tue 04 Jun-06 2019 19:55:14
"""
# * IMPORT

# * 3rd Party Library Imports
from termcolor import colored, cprint
from pyfiglet import Figlet, print_figlet, figlet_format
from examples import custom_style_2,custom_style_1

# * User Imports
from Exam import Exam
from ExamController import ExamController
from PyInquirer import style_from_dict, Token, prompt, Separator

def mode_run(mode) :
    """ Depending on the mode that the user chooses """ 

    switch={'Exams':exam_mode, 'Notes':notes_mode} # for some reason I cannot do like the mode_run I did for exam.py ...
    switch[mode]()

def exam_mode() :
    """ run the exam mode"""

    # Welcome Text
    text = "Are you ready for your exams ?"
    cprint(figlet_format(text, font="small"), "green", attrs=['bold'])

    # Init a exam controller
    controller = ExamController("exams_db.sqlite")

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

    # exitFlag = False
    # while exitFlag != True :
    #     answers = prompt(questions, style=custom_style_2)
    #     if controller.mode_run(answers['mode']) == True : # if it returns True, that means we want to exit frm this
    #         exitFlag = True 

    while True :
        answers = prompt(questions, style=custom_style_2)

        if answers['mode'] == 'Exit' :
            break

        controller.mode_run(answers['mode'])

    print("Done exam operations.")

def notes_mode() : 
    """ run the notes mode """

    # Welcome Text
    text = "Yeah, welcome to the club, pal."
    cprint(figlet_format(text, font="small"), "green", attrs=['bold'])

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