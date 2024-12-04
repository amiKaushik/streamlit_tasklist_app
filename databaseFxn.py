import sqlite3
conn = sqlite3.connect("data.db",check_same_thread=False)
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tasktable(user TEXT,task TEXT,task_status TEXT,task_due_date DATE)')

def add_data(user,task,task_status,task_due_date):
    c.execute('INSERT INTO tasktable(user,task,task_status,task_due_date) VALUES (?,?,?,?)',(user,task,task_status,task_due_date))
    conn.commit()

def view_all_data():
    c.execute('SELECT * FROM tasktable')
    data = c.fetchall()
    return data

def view_unique_tasks():
    c.execute('SELECT DISTINCT task FROM tasktable')
    data = c.fetchall()
    return data

def view_unique_user():
    c.execute('SELECT DISTINCT user FROM tasktable')
    data = c.fetchall()
    return data

#get task by task
def get_task(task):
    c.execute(f'SELECT * FROM tasktable WHERE task="{task}"')
    # c.execute('SELECT * FROM tasktable WHERE task=?',(task))
    data = c.fetchall()
    return data

#get task by user
def get_user(user):
    c.execute(f'SELECT * FROM tasktable WHERE user="{user}"')
    data = c.fetchall()
    return data

def edit_task_data(new_user,new_task,new_task_status,new_task_due_date,user,task,task_status,task_due_date):
    c.execute('UPDATE tasktable SET user=?,task =?,task_status=?,task_due_date=? WHERE user=? and task=? and task_status=? and task_due_date=?',(new_user,new_task,new_task_status,new_task_due_date,user,task,task_status,task_due_date))
    conn.commit()
    data = c.fetchall()
    return data

def delete_task(task):
    c.execute(f'DELETE FROM tasktable WHERE task="{task}"')
    conn.commit()