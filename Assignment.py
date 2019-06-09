"""
Author : Philippe Vo
Date : Tue 04 Jun-06 2019 19:17:37
"""

# * Imports

# * User imports
from Forms import AssignmentForm

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
              VALUES(?,?,?,?,?,?) '''
    removeSqlCmd = 'DELETE FROM assignments WHERE id=?'
    editSqlCmd = ''' UPDATE assignments
                SET classCode = ? ,
                    title = ?, 
                    date = ?,
                    daysLeft = ?,
                    totalNumbers = ?,
                    currentNumbers = ?,    
                    percentageDone= ?,                
                    filepath = ?
                WHERE id = ?'''
    editPercentageSqlCmd = ''' UPDATE assignments
                SET percentageDone = ?,
                currentNumbers = ?
                WHERE id = ?'''

    # This is the database file where the exams info will be stored
    databaseFile = "assignments_db.sqlite"

    def __init__(self,classCode = "", title="", filePath="", date="", daysLeft="",description="", totalNUmbers="", currentNumbers="", new = True) : 
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

            form = ExamForm()
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
            self.daysLeft = 0

            self.itemList = (self.classCode, self.title, self.date, self.daysLeft, self.currentNUmbers, self.totalNumbers, self.percentageDone, self.filepath)
