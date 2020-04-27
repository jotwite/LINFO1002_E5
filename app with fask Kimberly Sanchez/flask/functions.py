import sqlite3


def start():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
    return cursor, conn


def gradeforlinfo1101(cursor):
    lst = []
    lstask = []
    lstgrade = []
    for row in cursor.execute(''' SELECT DISTINCT course, task, grade FROM submissions WHERE course = "LSINF1101-PYTHON" LIMIT 150'''):
        lstask.append(row[1])
        lstgrade.append(row[2])

    lst = [lstask, lstgrade]
    
    return lst

def gradeforlinfo1252(cursor):
    lst = []
    lstask = []
    lstgrade = []
    for row in cursor.execute(''' SELECT DISTINCT course, task, grade FROM submissions WHERE course = "LSINF1252" LIMIT 150'''):
        lstask.append(row[1])
        lstgrade.append(row[2])

    lst = [lstask, lstgrade]
    
    return lst

def gradeforlepl1402(cursor):
    lst = []
    lstask = []
    lstgrade = []
    for row in cursor.execute(''' SELECT DISTINCT course, task, grade FROM submissions WHERE course = "LEPL1402" LIMIT 150'''):
        lstask.append(row[1])
        lstgrade.append(row[2])

    lst = [lstask, lstgrade]
    
    return lst

"""
def success(cursor):
    lst = []
    lstname = []
    lstrial = []
    for row in cursor.execute(''' SELECT DISTINCT task, result, course  FROM submissions WHERE course = "LSINF1101-PYTHON" LIMIT 100'''):
        lstname.append(row[0])
        lstrial.append(row[1])

    lst = [lstname, lstrial]

    return lst
"""


def close(conn):
    conn.close()

def main_for_grade1101():
    cursor, conn = start()
    data1 = gradeforlinfo1101(cursor)
    close(conn)

    return data1


def main_for_grade1252():
    cursor, conn = start()
    data2 = gradeforlinfo1252(cursor)
    close(conn)

    return data2

def main_for_grade1402():
    cursor, conn = start()
    data3 = gradeforlepl1402(cursor)
    close(conn)

    return data3
