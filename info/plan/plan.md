# School CLI Application
Mon 27 May 2019 03:11:28 PM EDT

--- 

website that might help : https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df

# Idea

Goal : Make school life better and efficient. Have a CLI like application used
by scukless.

How ?
- Documenting Homework
- Reminding : 
    - when exams are
    - when labs are
    - when labs reports are due
    - when assignments are due
- List all the homeworks due

- Notifies when one class has received more attention than the others
- Records how much time I spent on a class compared to the others

# WorkFlow

- class begins : 
- - record exams dates
- - record assignments due dates 
- - record lab dates
- - record homeworks todo

- everyday use : 
- - start app
        - shows all the exames dates and everything todo with a countdown on
            how many days left. 
        - shows all the assignments date 
        - shows all the homework left todo and when they are due
- - commands :
- - -help
- -     - shows all possible commands 
- - - dates :
- -     shows the dates due for everything
- - - exams : 
- -     shows all the info for exams.
- -     shows also the dir where i can information about the exams
- -     shows also all the relevant md files about the exams.  

# Exams 

- Be able to :
- say when
- how much time left
- basic info like what will be on the exam
- how many hours spent studying on it

Nice to have :
- an actual calendar appearing so that I can see when it is 
- https://stackabuse.com/introduction-to-the-python-calendar-module/

```terminal
brainiac -exam

# shows all the exams in a table and when they are due

| Exam Name | Class Code + Number | Date of Exam | Days Left | Amount of Time Studied | 
+-----------+---------------------+--------------+-----------+------------------------+
| Midterm   | COEN 346            | 2019-05-23   | 5 days    | 14 hours Studied       | 

```