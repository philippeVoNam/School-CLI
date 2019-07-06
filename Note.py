"""
Author : Philippe Vo
Date : Fri 05 Jul-07 2019 22:17:40
"""

# * Imports
# * User imports
from Forms import NoteForm
# * 3rd party imports
from datetime import date, datetime
from dateutil.parser import parse
from termcolor import colored, cprint
import os

class Note:
    """
    class to store the information of notes

    Attributes 
    ----------
    - classCode 
    - title
    - tags
    - folderpath

    Methods
    ------- 
    - make_dir

    Logic Functions
    ---------------
    
    Helper Functions
    ----------------

    """

    # * Static Variables
    # Default Attributes
    headers = [['id','Class Code', 'Title', 'Date', 'Folderpath']]
    title = "Note"
    dbFile = "notes_db.sqlite"
    tableName = "notes"
    addSqlCmd = ''' INSERT INTO notes (classCode, title, date, folderpath)
              VALUES(?,?,?,?) '''
    removeSqlCmd = 'DELETE FROM labreports WHERE id=?'
    editSqlCmd = ''' UPDATE labreports
                SET classCode = ? ,
                    title = ?, 
                    date = ?, 
                    folderpath = ?
                WHERE id = ?'''
    createSqlCmd = 'CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, classCode VARCHAR, title VARCHAR, date VARCHAR, folderpath VARCHAR)'

    # This is the database file where the exams info will be stored
    databaseFile = "notes_db.sqlite"

    # Lab report Folderpath
    folderName = "/home/namv/Documents/Knowledge/Coding/CLI_Apps/School_CLI/Notes"

    # Edit String List
    editStringList = ["classCode", "title", "date", "folderpath"]

    def __init__(self,classCode = "", title="", date="", folderpath="", new = True) : 
    # def __init__(self, id = -1, new = True) : 
        """ constructor """

        if new == False : 
            # Init an exam 
            self.classCode = classCode
            self.title = title 
            self.date = date
            self.folderpath = folderpath

            # self.itemList = (self.classCode, self.date, self.daysLeft, self.percentageDone)

        else : # It's a New item
            form = NoteForm()
            form.run()
            info = form.get_form_info()

            # init the item that is going into the database
            self.classCode = info["classCode"]
            self.date = info["date"]
            self.title = info["title"]
            self.folderpath = self.make_dir(self.classCode, self.title)

            self.itemList = (self.classCode, self.title, self.date, self.folderpath)
    
    def make_dir(self, classCode, folderName) :
        """ makes the dir where all the files will be contained """
        classCode = classCode.replace(' ', '-')
        folderName = folderName.replace(' ', '-')
        folderpath = Note.folderName + "/" + classCode + "/" + folderName
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