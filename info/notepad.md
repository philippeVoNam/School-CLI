# Notepad 
Mon 27 May-05 2019 22:39:36

---

# @ Useful CLI Tools
Tue 28 May-05 2019 09:32:54

- General : https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df

- PyInquirer : to make the CLI interactive
- click : general CLI python framework 
- ncurses -> GUI for terminal
- taskwarrior API -> https://github.com/ralphbean/taskw
- table in terminal -> https://github.com/Robpol86/terminaltables
- SQLite -> database -> https://www.pythonforthelab.com/blog/storing-data-with-sqlite/

---

# @ Database to store the information
Tue 28 May-05 2019 09:33:21

https://www.pythonforthelab.com/blog/storing-data-with-sqlite/

Example to do : 

terminal : 
CMD : brainiac --exam
-> Show
-> Add
-> Remove
-> Calendar

CMD -> Select

Depending on selection : 

Show : 
Retrieves all the exams saved
Shows all the exams in a table format

Add : 
Ask for Class code 
Ask for date

Remove :
Remove Exam based on its ID (like in TaskWarrior)

---

# @ SQLite - How to use it
Sat 01 Jun-06 2019 14:46:58


### Create a table 

```python

import sqlite3

conn = sqlite3.connect('AA_db.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE experiments (name VARCHAR, description VARCHAR)')
conn.commit()

conn.close()

```

### Adding Data to table

```python

cur.execute('INSERT INTO experiments (name, description) VALUES (?, ?)',
            ('Another User', 'Another Experiment, even using " other characters"'))
conn.commit()

```

### Retreive Data from table

```python

cur.execute('SELECT * FROM experiments WHERE name="Aquiles"')
data_3 = cur.fetchall()
```

### Primary Key

```python

sql_command = """
DROP TABLE IF EXISTS experiments;
CREATE TABLE experiments (
    id INTEGER,
    name VARCHAR,
    description VARCHAR,
    PRIMARY KEY (id));
INSERT INTO experiments (name, description) values ("Aquiles", "My experiment description");
INSERT INTO experiments (name, description) values ("Aquiles 2", "My experiment description 2");
"""
cur.executescript(sql_command)
conn.commit()
```

### Relational Databases

```sql

DROP TABLE IF EXISTS experiments;
DROP TABLE IF EXISTS users;
CREATE TABLE  users(
    id INTEGER,
    name VARCHAR,
    email VARCHAR,
    phone VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id));
CREATE TABLE experiments (
    id INTEGER,
    user_id INTEGER,
    description VARCHAR ,
    perfomed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
    FOREIGN KEY (user_id) REFERENCES users(id));
```

---

# @ More Robust SQLite Python
Sat 01 Jun-06 2019 15:09:16

- http://www.sqlitetutorial.net/sqlite-python/create-tables/

---

# @ Edit specific part of an exam and leave everything else alone

- Edit
- Ask uer what they want to edit
- Ask if they are done with the edit
- Have a done option 
- While not done 

- Pseudocode : 
- quitFlag = false
- while quitFlag != True :
  - ans = ask_input
  - if ans == quit :
    - quitFlag = True
    - break

- ans = Ask_input()
- returns the string of what they want to edit
- based on that, we know which ones we want to keep intact
- must retrieve everything else
- cur.execute("SELECT * FROM exams WHERE id=?", (6,))
- data = cur.fetchall()
- print(data)
- examInfo[ans] -> return the index
   questions = [
        {
            'type': 'input',
            'name': ans,
            'message': ans + ":",
        }
    ]
- data[index] = answer_questions