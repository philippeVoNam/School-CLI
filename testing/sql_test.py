import sqlite3

# Connect to a database -> if does not exist -> create
conn = sqlite3.connect('AA_db.sqlite')

# Allows the execution of SQL code
cur = conn.cursor()

# Execution
# cur.execute('CREATE TABLE experiments (name VARCHAR, description VARCHAR)')
cur.execute('INSERT INTO experiments (name, description) values ("Aquiles", "My experiment description")')
cur.execute('INSERT INTO experiments (name, description) VALUES (?, ?)',
            ('Another User', 'Another Experiment, even using " other characters"'))

cur.execute('SELECT * FROM experiments')
data = cur.fetchall()

print(data)

# Saves the changes you made
conn.commit()

conn.close()

