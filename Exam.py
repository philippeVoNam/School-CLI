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

    def __init__(self, classCode, type, date, daysLeft, studyTime) : 
        """ constructor """

        # Init an exam 
        self.classCode = classCode
        self.type = type
        self.date = date
        self.daysLeft = daysLeft
        self.studyTime = studyTime

        # Default Attributes
        self.headers = ['id','Class Code','Type', 'Date', 'Days Left', 'Study Time']
        self.title = "Exams"
        self.dbFile = "exams_db.sqlite"
        self.tableName = "exams"