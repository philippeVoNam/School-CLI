"""
Author : Philippe Vo
Date : Tue 04 Jun-06 2019 19:17:37
"""

# * Imports
# * User imports
from Forms import LabReportForm
# * 3rd party imports
from datetime import date, datetime
from dateutil.parser import parse
from termcolor import colored, cprint
import os

class LabReport:
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
    headers = [['id','Class Code', 'Title', 'Date', 'Days Left', '# Done', '# Total', 'Percentage Done','Folderpath']]
    title = "LabReport"
    dbFile = "labreports_db.sqlite"
    tableName = "labreports"
    addSqlCmd = ''' INSERT INTO labreports (classCode, title, date, daysLeft, currentNumbers, totalNumbers, percentageDone, folderpath)
              VALUES(?,?,?,?,?,?,?,?) '''
    removeSqlCmd = 'DELETE FROM labreports WHERE id=?'
    editSqlCmd = ''' UPDATE labreports
                SET classCode = ? ,
                    title = ?, 
                    date = ?,
                    daysLeft = ?,
                    currentNumbers = ?,
                    totalNumbers = ?,    
                    percentageDone= ?,                
                    folderpath = ?
                WHERE id = ?'''
    editPercentageSqlCmd = ''' UPDATE labreports
                SET percentageDone = ?,
                currentNumbers = ?
                WHERE id = ?'''
    createSqlCmd = 'CREATE TABLE IF NOT EXISTS labreports (id INTEGER PRIMARY KEY, classCode VARCHAR, title VARCHAR, date VARCHAR, daysLeft VARCHAR, currentNumbers VARCHAR, totalNumbers VARCHAR, percentageDone VARCHAR, folderpath VARCHAR)'

    # This is the database file where the exams info will be stored
    databaseFile = "labreports_db.sqlite"

    # Lab report Folderpath
    folderName = "/home/namv/Documents/Knowledge/Coding/CLI_Apps/School_CLI/Labs"

    # Edit String List
    editStringList = ["classCode", "title", "date", "folderpath", "currentNumbers"]

    def __init__(self,classCode = "", title="", folderpath="", date="", daysLeft="",description="", totalNumbers="", currentNumbers="", new = True) : 
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
            self.folderpath = folderpath
            self.description = description

            self.itemList = (self.classCode, self.date, self.daysLeft, self.percentageDone)

        else : # It's a New item

            form = LabReportForm()
            form.run()
            info = form.get_form_info()

            # init the item that is going into the database
            self.classCode = info["classCode"]
            self.date = info["date"]
            self.title = info["title"]
            self.totalNumbers = info["totalNumbers"]
            self.currentNUmbers = 0
            self.percentageDone = 0
            self.daysLeft = self.days_left(self.date)
            self.folderpath = self.make_dir(self.classCode, self.title)

            self.itemList = (self.classCode, self.title, self.date, self.daysLeft, self.currentNUmbers, self.totalNumbers, self.percentageDone, self.folderpath)

    @staticmethod
    def days_left(givenDate) :
        """ Returns the number of days between the current date aand the given date """
        currentDate = datetime.now().date()
        daysLeft = givenDate - currentDate

        # Find out how many days left and if less than 5 -> make it bright red
        if daysLeft.days < 10 :
            daysLeft = str(daysLeft.days)
            daysLeft = colored(daysLeft,'white', 'on_red',attrs=['bold'])
        else :
            daysLeft = str(daysLeft.days)

        return daysLeft
    

    def make_dir(self, classCode, folderName) :
        """ makes the dir where all the files will be contained """
        classCode = classCode.replace(' ', '-')
        folderName = folderName.replace(' ', '-')
        folderpath = LabReport.folderName + "/" + classCode + "/" + folderName
        os.system("mkdir -p " + folderpath) # -p creates the in between dir if they dont exist

        # create folder info
        folderPathInfo = folderpath + "/info"
        os.system("mkdir -p " + folderPathInfo)
        self.create_info_file(folderPathInfo, "notepad.md")
        self.create_info_file(folderPathInfo, "todo.md")
        self.create_info_file(folderPathInfo, "issues.md")

        return folderpath

    def create_info_file(self, folderpath, fileName) :
        """ creates default info files """
        fn = folderpath + "/" + fileName 
        file = open(fn, 'w+')

        # Building the description text 
        authorLabel = "Author   : " + "Philippe Vo" + "\n"
        dateLabel  = "Date     : " + datetime.now().strftime("%I:%M%p on %B %d, %Y")

        info = [authorLabel,dateLabel]
        file.writelines(info)