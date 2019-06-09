""" 
Author : Philippe Vo
Date : Fri 07 Jun-06 2019 22:49:23
"""

# * Imports

# * 3rd Library Imports
# * imports for the PyInquirer
from pprint import pprint
from PyInquirer import style_from_dict, prompt, Separator
from examples import custom_style_2,custom_style_1
# * imports for the PyInquirer
from terminaltables import AsciiTable
from termcolor import colored, cprint

# * USER IMPORTS
from sql_helper import create_connection, create_exam, create_table, delete_exam, update_exam
from Forms import ExamForm, AssignmentForm, LabReportForm, HomeworkForm, NoteForm
from sql_helper import create_connection_db, add_item_db, remove_item_db


class SItemController:
    """
    Attributes
    ----------
    - (none)

    Methods
    -------
    * Displays
    - show in table

    * Inputs 
    - input the date 
    - input the type
    - input the classCode
    - input the ID
    - input description
    - input filepath

    * Database
    - add in database
    - remove from database
    - edit database entry

    * Logic functions
    - calculate number of days left
    - validate the date
    - calculate percentage done

    * Additional Files
    - info folder

    * Folder Managing
    - open relevant folder

    * File Managing
    - create file - with default text (template)
    - open file

    * Tagging
    - input tag
    - create tag
    - filtering system
    """

    def __init__(self) :

        default = 0

    # * Displays
    def show_table(self, itemClass) :
        """ shows the itemType information in a table in ther terminal """
        
        # Display title of table
        itemTitle = colored(itemClass.title,'green') 
        print("Item :  " + itemTitle)

        # Fetch all the exams from the database
        conn = create_connection(itemClass.dbFile)
        cur = conn.cursor()
        cur.execute('SELECT * FROM ' + itemClass.tableName)
        data = cur.fetchall()

        # Copy the header of the item
        tableData = itemClass.headers.copy()

        for ele in data : 
            
            tableData.append(ele)

        table = AsciiTable(tableData)
        print (table.table)

    # * Inputs

    # ! the form static method inside the class renders this method useless
    # def input_form(self, itemType) :
    #     """ opens a input form based on the one asked for """

    #     if "exam" == itemType :
    #         form = ExamForm()
    #         form.run()
    #         info = form.get_form_info()
    #     elif "assignment" == itemType :
    #         form = AssignmentForm()
    #         form.run()
    #         info = form.get_form_info()
    #     elif "labReport" == itemType :
    #         form = LabReportForm()
    #         form.run()
    #         info = form.get_form_info()
    #     elif "homework" == itemType :
    #         form = HomeworkForm()
    #         form.run()
    #         info = form.get_form_info()
    #     elif "note" == itemType :
    #         form = NoteForm()
    #         form.run()
    #         info = form.get_form_info()

    #     return info # dictionary with the input answers

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

    # * Database 
    def create_item(self, itemClass) :
        """ ask user for input and adds to the database for them """

        # * Creating item
        # Creating input and getting the answer

        item = itemClass(new = True)

        print(type(item))

        # * Adding to the database
        # Connecting to the database
        conn = create_connection_db(item.databaseFile)

        # Add to database
        add_item_db(conn, item)

        # * Exit from database
        conn.commit()
        conn.close()

    def delete_item(self, itemClass) :
        """ ask user which item they want to delete """

        # Show the table of specified item
        self.show_table(itemClass)

        # Ask User for the id of the item they want to remove 
        id = self.id_input()

        # * Adding to the database
        # Connecting to the database
        conn = create_connection_db(itemClass.databaseFile)

        # Remove item with id 
        remove_item_db(conn, itemClass, id)
        
        # * Exit from database
        conn.commit()
        conn.close()

    def modify_numbers_done(self) :
        """ ask the user which item they want to modify the numbers did """

        # Show the table of specified item
        self.show_table(itemClass)

        # Ask User for the id of the item they want to update 
        id = self.id_input()

        # Ask the User how many they did more 
        # * Ask user fo the # done
        questions = [
            {
                'type': 'input',
                'name': 'amount',
                'message': 'Amount done :',
            }
        ]

        answers = prompt(questions, style=custom_style_2)
        amount = answers['amount']

        # Get the current number done and the total

        # ! requires to get a specific attribute of an item

        # Calculate the percentage

        # * Editing the Percentage 
        # Connecting to the database
        conn = create_connection_db(itemClass.databaseFile)







    # * Logic Functions
    """ 
    - calculate number of days left
    - validate the date
    - calculate percentage done
    """
    def days_left(self, givenDate) :
        """ Returns the number of days between the current date aand the given date """

        currentDate = datetime.datetime.now().date()
        delta = givenDate - currentDate

        return delta.days

    def calculate_percentage(self, step, total) :
        """ calculates the percentage and provides a color as well -> returns a string """

        percentage = round((step * 100) / total)

        # Find out what is the percentage and give it a color for it 
        if percentage == 0 :
            percentage = colored(str(percentage) + " %",'white', 'on_red', attrs=['bold'])
        elif percentage <= 25 :
            percentage = colored(str(percentage) + " %",'blue', 'on_yellow', attrs=['bold'])
        elif percentage > 25 and percentage <= 50 :
            percentage = colored(str(percentage) + " %",'white', 'on_magenta', attrs=['bold'])
        elif percentage > 50 and percentage <= 75 :
            percentage = colored(str(percentage) + " %",'white', 'on_blue', attrs=['bold'])
        elif percentage > 75 and percentage <= 99 :
            percentage = colored(str(percentage) + " %",'white', 'on_cyan', attrs=['bold'])
        else :
            percentage = colored(str(percentage) + " %",'white', 'on_green', attrs=['bold'])

        return percentage 