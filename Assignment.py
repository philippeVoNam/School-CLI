"""
Author : Philippe Vo
Date : Tue 04 Jun-06 2019 19:17:37
"""

# * Imports

# * User imports
from Forms import AssignmentForm
from datetime import date, datetime
from dateutil.parser import parse
from termcolor import colored, cprint

class Assignment:
    """
    class to store the information of exams 

    Attributes 
    ----------
    - classCode
    - type
    - date of exam
    - days left
    - study time accumulated 

    Methods
    ------- 

    Logic Functions
    ---------------
    
    Helper Functions
    ----------------

    """

    # * Static Variables
    # Default Attributes
    headers = [['id','Class Code', 'Title', 'Date', 'Days Left', '# Done', '# Total', 'Percentage Done','Filepath']]
    title = "Assignments"
    dbFile = "assignments_db.sqlite"
    tableName = "assignments"
    addSqlCmd = ''' INSERT INTO assignments(classCode, title, date, daysLeft, currentNumbers, totalNumbers, percentageDone, filepath)
              VALUES(?,?,?,?,?,?,?,?) '''
    removeSqlCmd = 'DELETE FROM assignments WHERE id=?'
    editSqlCmd = ''' UPDATE assignments
                SET classCode = ? ,
                    title = ?, 
                    date = ?,
                    daysLeft = ?,
                    currentNumbers = ?,
                    totalNumbers = ?,    
                    percentageDone= ?,                
                    filepath = ?
                WHERE id = ?'''
    editPercentageSqlCmd = ''' UPDATE assignments
                SET percentageDone = ?,
                currentNumbers = ?
                WHERE id = ?'''
    createSqlCmd = 'CREATE TABLE IF NOT EXISTS assignments (id INTEGER PRIMARY KEY, classCode VARCHAR, title VARCHAR, date VARCHAR, daysLeft VARCHAR, currentNumbers VARCHAR, totalNumbers VARCHAR, percentageDone VARCHAR, filepath VARCHAR)'

    # Edit String List
    editStringList = ["classCode", "title", "date", "currentNumbers", "filepath"]

    # This is the database file where the exams info will be stored
    databaseFile = "assignments_db.sqlite"

    def __init__(self,classCode = "", title="", filePath="", date="", daysLeft="",description="", totalNumbers="", currentNumbers="", new = True) : 
    # def __init__(self, id = -1, new = True) : 
        """ constructor """

        if new == False : 
            # Init an exam 
            self.classCode = classCode
            self.title = title 
            self.date = date
            self.daysLeft = daysLeft
            self.totalNumbers = totalNumbers
            self.currentNUmbers = currentNumbers
            self.filepath = filePath
            self.description = description

            self.itemList = (self.classCode, self.date, self.daysLeft, self.percentageDone)

        else : # It's a New item

            form = AssignmentForm()
            form.run()
            info = form.get_form_info()

            # init the item that is going into the database
            self.classCode = info["classCode"]
            self.date = info["date"]
            self.title = info["title"]
            self.filepath = info["filepath"]
            self.totalNumbers = info["totalNumbers"]
            self.currentNUmbers = 0
            self.percentageDone = 0
            self.daysLeft = self.days_left(self.date)

            self.itemList = (self.classCode, self.title, self.date, self.daysLeft, self.currentNUmbers, self.totalNumbers, self.percentageDone, self.filepath)

    def days_left(self, givenDate) :
        " Returns the number of days between the current date aand the given date "

        currentDate = datetime.now().date()
        daysLeft = givenDate - currentDate

        # Find out how many days left and if less than 5 -> make it bright red
        if daysLeft.days < 10 :
            daysLeft = str(daysLeft.days)
            daysLeft = colored(daysLeft,'white', 'on_red',attrs=['bold'])
        else :
            daysLeft = str(daysLeft.days)

        return daysLeft
    


