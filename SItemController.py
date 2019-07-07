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
import os
import datetime
import calendar

# * USER IMPORTS
from sql_helper import create_connection, create_exam, create_table, delete_exam, update_exam
from Forms import ExamForm, AssignmentForm, LabReportForm, HomeworkForm, NoteForm
from sql_helper import create_connection_db, add_item_db, remove_item_db, get_item_attribute, create_table, set_item_percentage_db, set_item_attribute
from StopWatch import stopwatch

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
    
    * Interactive functions
    - run the stopwatch for time watch

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

    def create_db(self, itemClass) :
        """ creates the intial database with headers """
        print("Constructing database ...")

        # * Creating the database if it does not exist
        # Connecting to the database
        conn = create_connection_db(itemClass.databaseFile)

        # Create table if it doesnt exist
        create_table(conn, itemClass.createSqlCmd)

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

        print("Data Information ", data)

        # Copy the header of the item
        tableData = itemClass.headers.copy()

        for ele in data : 
            
            tableData.append(ele)

        table = AsciiTable(tableData)
        print (table.table)

    def show_calendar(self, itemClass) :
        """ show the calendar in the terminal """

        now = datetime.datetime.now()
        print(calendar.calendar(int(now.year), 2, 1, 1, 4))  
    
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

        # Create table if it doesnt exist
        create_table(conn, itemClass.createSqlCmd)

        # Add to database
        add_item_db(conn, item)

        # * Exit from database
        conn.commit()
        conn.close()

    def delete_item(self, itemClass) :
        """ ask user which item they want to delete """

        # Show the table of specified item
        # self.show_table(itemClass)

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

    def edit_item(self, itemClass) :
        """ lets user edit an item inside a itemClass """

        # Ask User for the id of the item they want to remove 
        id = self.id_input()

        # * Adding to the database
        # Connecting to the database
        conn = create_connection_db(itemClass.databaseFile)

        # * Have a mulit-line selection - ask user what they wanna change
        question = [
        {
            'type': 'list',
            'name': 'item',
            'message': 'What would you like to edit?',
            'choices': itemClass.editStringList
            },
        ]
        itemStringanswers = prompt(question, style=custom_style_2)
        itemString = itemStringanswers["item"]

        itemValQuestion = [
            {
                'type': 'input',
                'name': 'itemValue',
                'message': 'What\'s the value you want to change to ?',
            }
        ]

        # * Checking if they are special cases (ie. date,currentNumbers)
        if itemString == "date" :
            # Asking for date 
            answers = prompt(itemValQuestion, style=custom_style_2)
            date = answers["itemValue"]
            
            # Calculate the days left needed
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date() # converts string date into a date obj
            daysLeft = itemClass.days_left(date)

            # TODO -> ERROR : daysLeft in color not good with the sql execute command -> not sure why + not updating the table ... 
            editSqlCmd = "UPDATE " + itemClass.tableName + " SET " + itemString + " = ? " + ", daysLeft = ? WHERE id = ?"
            cur = conn.cursor()
            cur.execute(editSqlCmd, (str(date), daysLeft, id))

        elif itemString == "currentNumbers" :
            # Asking for currentNumber 
            answers = prompt(itemValQuestion, style=custom_style_2)
            currentNumber = int(answers["itemValue"])

            # Calculate the percentage 
            # TODO Calculate the percentage
            cur = conn.cursor()
            cur.execute('SELECT totalNumbers FROM ' + itemClass.tableName + " WHERE id = " + str(id))
            totalNumbers = int(cur.fetchone()[0])
            percentage = self.calculate_percentage(currentNumber,totalNumbers)

        elif itemString == "folderpath" or itemString == "filepath" :
            # Show folder explorer to get folderpath
            from PySide2.QtWidgets import QFileDialog, QApplication
            import sys
            app = QApplication(sys.argv)
            folderpath = QFileDialog.getExistingDirectory()

            editSqlCmd = "UPDATE " + itemClass.tableName + " SET " + itemString + " = ? "  + " WHERE id = ?"
            cur = conn.cursor()
            cur.execute(editSqlCmd, (folderpath, id))
    

        else :
            # Asking for Value 
            answers = prompt(itemValQuestion, style=custom_style_2)
            itemValue = answers["itemValue"]
            editSqlCmd = "UPDATE " + itemClass.tableName + " SET " + itemString + " = ? "  + " WHERE id = ?"
            cur = conn.cursor()
            cur.execute(editSqlCmd, (itemValue, id))
    
        # ! IF EDIT DATE -> AUTOMATICALLY UPDATE DAYS_LEFTIC -> PERCEnTAGE CHANGE 
        # ! ID EDIT CURRENT_NUMBERS -> UPDATE PECENTAGE
        
        # TODO depending on what they want to change -> input / folderpath / date ... 

        # cur = conn.cursor()
        # cur.execute('SELECT ' + itemToChange + ' FROM exams')
        # data = cur.fetchall()

        # * User can then modify the form to make their changes and then change 

        # * pass the update itemlist

        # * Exit from database
        conn.commit()
        conn.close()

    def modify_numbers_done(self, itemClass) :
        """ ask the user which item they want to modify the numbers did """

        # Show the table of specified item
        # self.show_table(itemClass)

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

        # * Editing the Percentage 
        # Connecting to the database
        conn = create_connection_db(itemClass.databaseFile)

        # Get the current number done and the total
        currentNumber = get_item_attribute(conn, itemClass,"currentNumbers",id)
        currentNumber = int(currentNumber) + int(amount)

        totalNumber = get_item_attribute(conn, itemClass,"totalNumbers",id)
        totalNumber = int(totalNumber)

        # Calculating the percentage
        percentage = self.calculate_percentage(currentNumber,totalNumber)

        # Edit the percentage
        set_item_percentage_db(conn, itemClass, percentage, currentNumber, id)

        # * Exit from database
        conn.commit()
        conn.close()

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

    # * Interactive functions
    def record_study_time(self, itemClass) :
        """ starts a stopwatch and records the time, when the users stop it -> appends the time to the exam """

        # Ask the user for the exam they want to record tihe study time
        id = self.id_input()

        # Start the stopwatch        
        currentTime = stopwatch()
        currentTime = datetime.timedelta(seconds=round(currentTime)) # convert float to time obj

        # Retrieve the study time of the given id 
        conn = create_connection(itemClass.databaseFile)
        # Get the studyTime
        data = get_item_attribute(conn, itemClass,"studyTime",id)

        # Constructing the datetime.time obj from string
        retrievedTime = datetime.datetime.strptime(str(data), '%H:%M:%S').time()
        retrievedTime = datetime.timedelta(hours=retrievedTime.hour, minutes=retrievedTime.minute, seconds=retrievedTime.second) # converting the time to timedelta
        
        # Appending the time 
        totalTime = str((currentTime + retrievedTime))

        # Updating the database
        set_item_attribute(conn, itemClass, "studyTime", totalTime, id)

        # Closing the database
        conn.commit()
        conn.close()

    # * File Managing
    def view_file(self, itemClass) :
        """ opens file in default program """

        # Show the table of specified item
        # self.show_table(itemClass)

        # Ask User for the id of the item they want to view
        id = self.id_input()

        # * View File
        # Connecting to the database
        conn = create_connection_db(itemClass.databaseFile)
        # Get the filepath
        filepath = get_item_attribute(conn, itemClass,"filepath",id)

        os.system("evince " + filepath)

    # * Folder Managing
    def view_folder(self, itemClass) :
        #    """ open folder in ranger """

        # Show the table of specified item
        # self.show_table(itemClass)

        # Ask User for the id of the item they want to view
        id = self.id_input()

        # * View File
        # Connecting to the database
        conn = create_connection_db(itemClass.databaseFile)
        # Get the folderpath
        folderpath = get_item_attribute(conn, itemClass,"folderpath",id)

        os.system("ranger " + folderpath)

    # * Update whole tables
    def update_daysLeft(self, itemClasses) :
        """ goes over all the tables with daysLeft and update them depending on the current date """
        # iterate over the tables
        files = ["assignments_db.sqlite", "labreports_db.sqlite", "exams_db.sqlite"]
        tableNames = ["assignments", "labreports", "exams"]

        # ! expecting -> itemClasses = [Assignment, LabReport, Exam]

        # iterate over the itemClass

        for itemClass in itemClasses :
            
            # * Adding to the database
            # Connecting to the database
            conn = create_connection_db(itemClass.databaseFile)
            cur = conn.cursor()

            print(itemClass.tableName)

            for row in cur.execute('SELECT date, id FROM ' + itemClass.tableName):
                days = 0

                # TODO -> Getting a weird error of "NoteType" -> but the date is there ???
                # get the due date
                date = cur.fetchone()[0]
                id = cur.fetchone()[1]
                print(date)
                dueDate = datetime.datetime.strptime(date, '%Y-%m-%d').date() # converts string date into a date obj

                # calculate the daysLeft
                daysLeft = itemClass.days_left(dueDate)
                print(daysLeft)

                # update table 
                # cur.execute("UPDATE " + itemClass.tableName + " SET daysLeft = ? WHERE id= ?", (daysLeft, id))

                # close table