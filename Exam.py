"""
Author : Philippe Vo
Date : Tue 04 Jun-06 2019 19:17:37
"""

# * Imports

# * User imports
from Forms import ExamForm

class Exam:
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
    headers = [['id','Class Code','Type', 'Date', 'Days Left', 'Study Time']]
    title = "Exams"
    dbFile = "exams_db.sqlite"
    tableName = "exams"
    addSqlCmd = ''' INSERT INTO exams(classCode, type, date, daysLeft, studyTime)
              VALUES(?,?,?,?,?) '''
    removeSqlCmd = 'DELETE FROM exams WHERE id=?'
    editSqlCmd = ''' UPDATE exams
                SET classCode = ? ,
                    type = ? ,
                    date = ?,
                    daysLeft = ?,
                    studyTime = ?
                WHERE id = ?'''

    # This is the database file where the exams info will be stored
    databaseFile = "exams_db.sqlite"

    def __init__(self,classCode = "", type="", date="", daysLeft="", studyTime="", new = True) : 
    # def __init__(self, id = -1, new = True) : 
        """ constructor """

        if new == False : 
            # Init an exam 
            self.classCode = classCode
            self.type = type
            self.date = date
            self.daysLeft = daysLeft
            self.studyTime = studyTime

            self.itemList = (self.classCode, self.type, self.date, self.daysLeft, self.studyTime)

        else : # It's a New item

            form = ExamForm()
            form.run()
            info = form.get_form_info()

            self.classCode = info["classCode"]
            self.type = info["type"]
            self.date = info["date"]
            self.daysLeft = 1
            self.studyTime = 1

            self.itemList = (self.classCode, self.type, self.date, self.daysLeft, self.studyTime)
