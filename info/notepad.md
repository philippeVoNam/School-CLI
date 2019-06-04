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

# @ How to calculate the amount of time studied ?
Sun 02 Jun-06 2019 22:19:58

- idea :
in the school app :

- exam info
- exam timing

- exam timing : 
  - checks the exams_db
  - return a list of exams
  - ask you which one you want to monitor
  - -> gets the id so that it can modify the study time when finished
  - starts a stopwatch -> you can cancel anytime using q ?
  - stopped -> adds the time that it recorded to the amount of time it already has 

---

# @ Stopwatch -> register in table
Tue 04 Jun-06 2019 18:52:52

Flow :
- Open app
- Open exam section
- Open stopwatch option
- This will "show" the available exms
- It will then ask for the id you want to record the study time. 
- Then it will start the stopwatch -> possible animation 
- User stops the study section 
- Retrieve the study time of the id
- Append the new time to the old time and register the result into the table

TODO : 
* [ ] multiple menu -> (exam , homework) 
* [ ] make exam class -> might need a re-definition of how stuff is being sent to the sql_helper functions 
* [ ] stopwatch option -> stopwatch function

---

# @ Exam as a class

class Exam : 
attributes :
- Class Code
- type
- Date due
- Study time accumulated 

Why would we need an object here. 
We would need, when we need to read in individually exams ... 
So that it is easy to get its individual attributes

--- 

# Homework quick preview plan 
Tue 04 Jun-06 2019 18:50:00

• Exam 
1. Name
2. Date
3. Location 

Goal : to store homework exercises and general notes better. With tags !

Written study notes.
Then take picture of it. 
Writing text to computer text
Sorts it into the correct folder
And puts tags on it for later search
ing and documentation

Homework exercises. 
Tags. 
Number the exercises. Detect that.

Flow : 
Take writing notes.
Put tags.
Upload to photos.
Download to desktop.
Open school CLI
Go to Homework and Notes mode
Go to add pictures
Pass in the file path
Store the file in correct directory given the tags analyzed.

Have the outlines in the application. 
Can open anytime in PDF 

Homework class
Easy.medium.hard.final exam level
Progress bar percentage done
Date
Folder where it is. Image 
Tags

Use the expand tab of PyInquirer

Make the app executable from CLI

If OCR really does not work,
Just write down the tags you think are appropriate. And then when you put in Computer, just write them down. 

How to make TAGS with Sqlite

Expands types of tags ???
Create new tags

---