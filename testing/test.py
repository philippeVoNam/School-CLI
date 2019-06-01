from pyfiglet import Figlet
import sqlite3
import calendar

import click

@click.command()
@click.option('--add',default="COEN 346")
def main(add) : 
    f = Figlet(font='slant')
    print(f.renderText('Are you ready for your exams ?'))
    # classCode = input("Class Code : ")
    # print ("Calendar of March 2019 is:")  
    # print (calendar.TextCalendar(calendar.SUNDAY).formatyear(2019, 2, 1, 1, 4))
    # # date = input("Date : ")
    print(add)
    print(type(add))

if __name__ == '__main__' : 
    main()

# # * SQLLite 

# # Connect to a database -> if does not exist -> create
# conn = sqlite3.connect('exams_db.sqlite')

# # Allows the execution of SQL code
# cur = conn.cursor()

# # Execution
# cur.execute('CREATE TABLE exams (classCode VARCHAR, date VARCHAR)')
# cur.execute('INSERT INTO experiments (name, description) values ("Aquiles", "My experiment description")')
# cur.execute('INSERT INTO experiments (name, description) VALUES (?, ?)',
#             ('Another User', 'Another Experiment, even using " other characters"'))