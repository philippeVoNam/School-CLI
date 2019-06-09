""" 
Author : Philippe Vo
Date : Fri 07 Jun-06 2019 22:49:23
"""

# * Imports
# * 3rd Library Imports
from terminaltables import AsciiTable
from termcolor import colored, cprint

# * USER IMPORTS
from sql_helper import create_connection, create_exam, create_table, delete_exam, update_exam
from Forms import ExamForm, AssignmentForm, LabReportForm, HomeworkForm, NoteForm


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
    def show_table(self, item) :
        """ shows the itemType information in a table in ther terminal """
        
        # Display title of table
        itemTitle = colored(item.title,'green') 
        print("Item :  " + itemTitle)

        # Fetch all the exams from the database
        conn = create_connection(item.dbFile)
        cur = conn.cursor()
        cur.execute('SELECT * FROM ' + item.tableName)
        data = cur.fetchall()

        # Copy the header of the item
        tableData = item.headers.copy()

        for ele in data : 
            
            tableData.append(ele)

        table = AsciiTable(tableData)
        print (table.table)

    # * Inputs
    def input_form(self, itemType) :
        """ opens a input form based on the one asked for """

        if "exam" == itemType :
            form = ExamForm()
            form.run()
            info = form.get_form_info()
        elif "assignment" == itemType :
            form = AssignmentForm()
            form.run()
            info = form.get_form_info()
        elif "labReport" == itemType :
            form = LabReportForm()
            form.run()
            info = form.get_form_info()
        elif "homework" == itemType :
            form = HomeworkForm()
            form.run()
            info = form.get_form_info()
        elif "note" == itemType :
            form = NoteForm()
            form.run()
            info = form.get_form_info()

        return info # dictionary with the input answers

    # * Database
    # add
    def add(self, conn, item):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        sql = item.addSqlCmd
        cur = conn.cursor()
        print(item.itemList)
        cur.execute(sql, item.itemList)
        return cur.lastrowid





    
