"""
Author : Philippe Vo
Date : Tue 04 Jun-06 2019 19:17:37
"""

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

    def __init__(self, classCode, type, date, daysLeft, studyTime) : 
        """ constructor """

        # Init an exam 
        self.classCode = classCode
        self.type = type
        self.date = date
        self.daysLeft = daysLeft
        self.studyTime = studyTime

        self.itemList = (self.classCode, self.type, self.date, self.daysLeft, self.studyTime)