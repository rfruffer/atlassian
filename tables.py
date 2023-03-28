import sqlite3

def createTables():
    conn = sqlite3.connect('Tables.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS Task (
        Reporter INTEGER UNIQUE,
        Summary TEXT,
        Description TEXT,
        Project TEST,
        Temp TEXT
    );
    ''')
    conn.commit()

    c.close()
    conn.close()

def setReporter(User_id):
    conn = sqlite3.connect('Tables.db')
    c = conn.cursor()
    sql = "INSERT OR IGNORE INTO Task (Reporter) VALUES (?)"
    c.execute(sql, (User_id,))
    conn.commit()
    c.close()
    conn.close()

def setDescription(Description, User_id):
    conn = sqlite3.connect('Tables.db')
    c = conn.cursor()
    sql = "UPDATE Task SET Description=?,Summary=?,Project=?, Temp=? where Reporter=?"
    c.execute(sql, (Description, "Awaiting", "Awaiting", None, User_id,))
    conn.commit()
    c.close()
    conn.close()

def setSummary(Summary, User_id):
    conn = sqlite3.connect('Tables.db')
    c = conn.cursor()
    sql = "UPDATE Task SET Summary=? where Reporter=?"
    c.execute(sql, (Summary, User_id,))
    conn.commit()
    c.close()
    conn.close()

def setProject(Project, User_id):
    conn = sqlite3.connect('Tables.db')
    c = conn.cursor()
    sql = "UPDATE Task SET Project=? where Reporter=?"
    c.execute(sql, (Project, User_id,))
    conn.commit()
    c.close()
    conn.close()

def setTemp(Project, User_id):
    conn = sqlite3.connect('Tables.db')
    c = conn.cursor()
    sql = "UPDATE Task SET Temp=? where Reporter=?"
    c.execute(sql, (Project, User_id,))
    conn.commit()
    c.close()
    conn.close()

def sql_getDescription(user):
    conn = sqlite3.connect('Tables.db')
    c = conn.cursor()
    sql = "SELECT Description FROM Task WHERE Reporter=?"
    c.execute(sql, (user,))
    return (c.fetchone()[0])

def sql_getSummary(user):
    conn = sqlite3.connect('Tables.db')
    c = conn.cursor()
    sql = "SELECT Summary FROM Task WHERE Reporter=?"
    c.execute(sql, (user,))
    return (c.fetchone()[0])

def sql_getProject(user):
    conn = sqlite3.connect('Tables.db')
    c = conn.cursor()
    sql = "SELECT Project FROM Task WHERE Reporter=?"
    c.execute(sql, (user,))
    return (c.fetchone()[0])

def sql_getTemp(user):
    conn = sqlite3.connect('Tables.db')
    c = conn.cursor()
    sql = "SELECT Temp FROM Task WHERE Reporter=?"
    c.execute(sql, (user,))
    return (c.fetchone()[0])
