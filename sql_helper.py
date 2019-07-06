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

# ! new version here 

def create_connection_db(itemDatabaseFile) :
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(itemDatabaseFile)
        return conn
    except sqlite3.Error as e:
        print(e)
 
    return None

def add_item_db(conn, item) :
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    print(len(item.itemList))
    sql = item.addSqlCmd
    cur = conn.cursor()
    cur.execute(sql, item.itemList)
    return cur.lastrowid

def remove_item_db(conn, itemClass, id) :
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    cur = conn.cursor()
    cur.execute(itemClass.removeSqlCmd, (id,))

def edit_item_db(conn, item, itemList) :
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    cur = conn.cursor()
    currentList = item.itemList + (id,)
    cur.execute(item.editSqlCmd, currentList)

def set_item_percentage_db(conn, itemClass, percentage, currentNumbers, id) :
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    cur = conn.cursor()
    cur.execute(itemClass.editPercentageSqlCmd, (percentage, currentNumbers, id))

def get_item_attribute(conn, itemClass, attribute, id) :
    """
    get a single attribute from a item with id
    :param conn:
    :param task:
    :return: project id
    """
    cur = conn.cursor()
    sqlCmd = "SELECT " + attribute + " FROM " + itemClass.tableName +" WHERE id=?"
    cur.execute(sqlCmd, (id,))
    data = cur.fetchone()

    return data[0]

def set_item_attribute(conn, itemClass, attribute, value, id) :
    """
    get a single attribute from a item with id
    :param conn:
    :param task:
    :return: project id
    """
    cur = conn.cursor()
    sqlCmd = "SELECT " + attribute + " FROM " + itemClass.tableName + " WHERE id=?"
    sqlCmd = "UPDATE " + itemClass.tableName + " SET " + attribute + " = ? " + " WHERE id=?"
    cur.execute(sqlCmd, (value,id))