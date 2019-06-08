""" 
Author : Philippe Vo
Date : Fri 07 Jun-06 2019 22:49:23
"""

# * Imports
from terminaltables import AsciiTable

class SItemController:
    """
    Attributes
    ----------
    - (none)

    Methods
    -------
    * Displays
    - show in table

    * Logic functions
    - calculate number of days left
    - validate the date
    - calculate percentage done

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
        itemTitle = colored(item.title,'Green') 
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




    
