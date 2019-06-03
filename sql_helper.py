""" 
Author : Philippe Vo
Date : Sat 01 Jun-06 2019 15:11:23
"""

# IMPORTS

import sqlite3

# * Helper Functions

# Create a connection with a database 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
 
    return None

# Create a table 

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

# Inserting data into Table

def create_exam(conn, classCode, type, date, daysLeft, studyTime):
    """
    Create a new exam into the exams table
    :param conn:
    :param exam:
    :return: 
    """
    sql = ''' INSERT INTO exams(classCode, type, date, daysLeft, studyTime)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (classCode, type, date, daysLeft, studyTime))
    return cur.lastrowid

def delete_exam(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM exams WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))

def update_exam(conn, id, classCode, type, date, daysLeft, studyTime):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE exams
              SET classCode = ? ,
                  type = ? ,
                  date = ?,
                  daysLeft = ?,
                  studyTime = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (classCode, type, date, daysLeft, studyTime,id))

# conn = create_connection("test_db.sqlite")

# create_table(conn, 'CREATE TABLE IF NOT EXISTS exams (classCode VARCHAR, date VARCHAR)')

# create_exam(conn,"COEN 346", "2019-05-31")
# create_exam(conn,"ELEC 312", "2019-06-01")

# cur = conn.cursor()
# cur.execute('SELECT * FROM exams')
# data = cur.fetchall()

# print(data)