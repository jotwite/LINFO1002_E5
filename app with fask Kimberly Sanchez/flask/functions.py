import sqlite3

"""
DESCRIPTIONS :

Ci-dessous,

Vous allez trouvé:
- une fonction Start()      : qui ouvre la base de donnée SQL

- 3 fonctions* pour les 3 cours qui sont dans la base de donnée.

- une fonction Close()      : qui ferme la base donnée.

- 3 fonctions main_for_...  : qui appellent les 3 fonctions précedents.

*:
Dans chaque fonction, je crée 3 listes:
    1. lst     : qui stocke 2 listes en mode [x,y]
    2. lstask  : qui stocke les premiers 150 tâches qui étaient à faire pour le cours "course" en ordre croissant
    3. lstgrade: qui stocke la moyenne de réussite de chaque tâche.
    
Après cela, j'ajoute lstask et lstgrade dans lst pour representer x et y respectivement.
Donc sur notre site, mon graphe aura:
comme x: les tâches.
comme y: la moyenne de réussite pour chaque tâches.

"""

def start():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
    return cursor, conn


def gradeforlsinf1101(cursor):
    """
        Je rentre dans la base de donnée dans la partie "submissions".
        Pour le cours de "LSINF1101-PYTHON", je prends les 150 premières tâches et leur moyenne de réussite et le stocke dans 2 listes separement.
        Je trie les 2 listes.
        Je retourne la liste qui contient les 2 listes    
    """
    lst = []
    lstask = []
    lstgrade = []
    for row in cursor.execute(''' SELECT DISTINCT course, task, grade FROM submissions WHERE course = "LSINF1101-PYTHON" LIMIT 150'''):
        lstask.append(row[1])
        lstgrade.append(row[2])
        lstask.sort()
        lstgrade.sort()

    lst = [lstask, lstgrade]
    
    return lst

def gradeforlsinf1252(cursor):
    """
        Je rentre dans la base de donnée dans la partie "submissions".
        Pour le cours de "LSINF1252", je prends les 150 premières tâches et leur moyenne de réussite et le stocke dans 2 listes separement.
        Je trie les 2 listes.
        Je retourne la liste qui contient les 2 listes
        
    """
    lst = []
    lstask = []
    lstgrade = []
    for row in cursor.execute(''' SELECT DISTINCT course, task, grade FROM submissions WHERE course = "LSINF1252" LIMIT 150'''):
        lstask.append(row[1])
        lstgrade.append(row[2])
        lstask.sort()
        lstgrade.sort()

    lst = [lstask, lstgrade]
    
    return lst

def gradeforlepl1402(cursor):
    """
        Je rentre dans la base de donnée dans la partie "submissions".
        Pour le cours de "LEPL1402", je prends les 150 premières tâches et leur moyenne de réussite et le stocke dans 2 listes separement.
        Je trie les 2 listes.
        Je retourne la liste qui contient les 2 listes
    """
    lst = []
    lstask = []
    lstgrade = []
    for row in cursor.execute(''' SELECT DISTINCT course, task, grade FROM submissions WHERE course = "LEPL1402" LIMIT 150'''):
        lstask.append(row[1])
        lstgrade.append(row[2])
        lstask.sort()
        lstgrade.sort()

    lst = [lstask, lstgrade]

    return lst

#-----------------LSINF1101---------------------------------------------------------------------
#-----------Page d'accueil--------------------------------------------------------------------

def LSINF1101(cursor):
    "nombre total de soumissions pour chaque tâche "
    values = []
    cursos= []
    frecuencia = []
    lst = []
    for row in cursor.execute('''SELECT course,grade,task FROM submissions WHERE course = "LSINF1101-PYTHON"'''):
        if row[2] not in cursos:
            cursos.append(row[2])
    for row in cursor.execute('''SELECT course,grade,task FROM submissions WHERE course = "LSINF1101-PYTHON"'''):
        values.append(row[2])
    for i in cursos:
        frecuencia.append((values.count(i),i))
    frecuencia = sorted(frecuencia)
    values = []
    cursos = []
    for i in range(len(frecuencia)):
        values.append(frecuencia[i][0])
        cursos.append(frecuencia[i][1])
    lst = [values,cursos]

    return lst

#----------------- LSINF1252---------------------------------------------------------------------
#-----------Page d'accueil--------------------------------------------------------------------

def LSINF1252(cursor):
    "nombre total de soumissions pour chaque tâche "
    values = []
    cursos= []
    frecuencia = []
    for row in cursor.execute('''SELECT course,grade,task FROM submissions WHERE course = "LSINF1252"'''):
        if row[2] not in cursos:
            cursos.append(row[2])
    for row in cursor.execute('''SELECT course,grade,task FROM submissions WHERE course = "LSINF1252"'''):
            values.append(row[2])
    for i in cursos:
        frecuencia.append((values.count(i),i))
    frecuencia = sorted(frecuencia)
    values = []
    cursos = []
    for i in range(len(frecuencia)):
        values.append(frecuencia[i][0])
        cursos.append(frecuencia[i][1])
    lst = [values,cursos]

    return lst

#----------------Page d'accueil---------------------------------------------
#----------------LEPL1402---------------------------------------------

def LEPL1402(cursor):
    "nombre total de soumissions pour chaque tâche "
    labels = []
    values = []
    cursos= []
    frecuencia = []
    for row in cursor.execute('''SELECT course,grade,task FROM submissions WHERE course = "LEPL1402"'''):
        if row[2] not in cursos:
            cursos.append(row[2])
    for row in cursor.execute('''SELECT course,grade,task FROM submissions WHERE course = "LEPL1402"'''):
            values.append(row[2])
    for i in cursos:
        frecuencia.append((values.count(i),i))
    frecuencia = sorted(frecuencia)
    values = []
    cursos = []
    for i in range(len(frecuencia)):
        values.append(frecuencia[i][0])
        cursos.append(frecuencia[i][1])
    lst =[values,cursos]

    return lst

#----------------------------------------------------------------
#____________Montly Sumissions___________________________________
#____________LSINF1252___________________________________________

def generalLSINF1252(cursor):
    "total des soumissions mensuelles "
    values1 = 0
    values2 = 0
    values3 = 0
    values4 = 0
    values5 = 0
    values6 = 0
    values7 = 0
    values8 = 0
    values9 = 0
    values10 = 0
    values11 = 0
    values = []
    for row in cursor.execute('''SELECT course, submitted_on FROM submissions WHERE course = "LSINF1252"'''):
        if '2019' in row[1] and '02' in row[1]:
            values1 += 1
        if '2019' in row[1] and '03' in row[1]:
            values2 += 1
        if '2019' in row[1] and '04' in row[1]:
            values3 += 1
        if '2019' in row[1] and '05' in row[1]:
            values4 += 1
        if '2019' in row[1] and '06' in row[1]:
            values5 += 1
        if '2019' in row[1] and '07' in row[1]:
            values6 += 1
        if '2019' in row[1] and '08' in row[1]:
            values7 += 1
        if '2019' in row[1] and '09' in row[1]:
            values8 += 1
        if '2019' in row[1] and '10' in row[1]:
            values9 += 1
        if '2019' in row[1] and '11' in row[1]:
            values10 += 1
        if '2019' in row[1] and '12' in row[1]:
            values11 += 1
    values.append(values1)
    values.append(values2)
    values.append(values3)
    values.append(values4)
    values.append(values5)
    values.append(values6)
    values.append(values7)
    values.append(values8)
    values.append(values9)
    values.append(values10)
    values.append(values11)

    return values

#----------------------------------------------------------------
#____________Montly Sumissions___________________________________
#____________LSINF1252___________________________________________

def generalLSINF1101(cursor):
    "total des soumissions mensuelles "
    values1 = 0
    values2 = 0
    values3 = 0
    values4 = 0
    values5 = 0
    values6 = 0
    values7 = 0
    values8 = 0
    values9 = 0
    values10 = 0
    values11 = 0
    values = []
    for row in cursor.execute('''SELECT course, submitted_on FROM submissions WHERE course = "LSINF1101-PYTHON"'''):
        if '2019' in row[1] and '02' in row[1]:
            values1 += 1

        if '2019' in row[1] and '03' in row[1]:
            values2 += 1

        if '2019' in row[1] and '04' in row[1]:
            values3 += 1

        if '2019' in row[1] and '05' in row[1]:
            values4 += 1

        if '2019' in row[1] and '06' in row[1]:
            values5 += 1

        if '2019' in row[1] and '07' in row[1]:
            values6 += 1
        if '2019' in row[1] and '08' in row[1]:
            values7 += 1
        if '2019' in row[1] and '09' in row[1]:
            values8 += 1
        if '2019' in row[1] and '10' in row[1]:
            values9 += 1
        if '2019' in row[1] and '11' in row[1]:
            values10 += 1
        if '2019' in row[1] and '12' in row[1]:
            values11 += 1
    values = [values1,values2,values3,values4,values5,values6,values7,values8,values9,values10,values11]

    return values

#----------------------------------------------------------------
#____________Montly Sumissions___________________________________
#____________LEPL1402___________________________________________

def generalLEPL1402(cursor):
    "total des soumissions mensuelles "
    values1 = 0
    values2 = 0
    values3 = 0
    values4 = 0
    values5 = 0
    values6 = 0
    values7 = 0
    values8 = 0
    values9 = 0
    values10 = 0
    values11 = 0
    values = []
    for row in cursor.execute('''SELECT course, submitted_on FROM submissions WHERE course = "LEPL1402"'''):
        if '2019' in row[1] and '02' in row[1]:
            values1 += 1

        if '2019' in row[1] and '03' in row[1]:
            values2 += 1

        if '2019' in row[1] and '04' in row[1]:
            values3 += 1

        if '2019' in row[1] and '05' in row[1]:
            values4 += 1

        if '2019' in row[1] and '06' in row[1]:
            values5 += 1

        if '2019' in row[1] and '07' in row[1]:
            values6 += 1
        if '2019' in row[1] and '08' in row[1]:
            values7 += 1
        if '2019' in row[1] and '09' in row[1]:
            values8 += 1
        if '2019' in row[1] and '10' in row[1]:
            values9 += 1
        if '2019' in row[1] and '11' in row[1]:
            values10 += 1
        if '2019' in row[1] and '12' in row[1]:
            values11 += 1
    values = [values1,values2,values3,values4,values5,values6,values7,values8,values9,values10,values11]
    return values

#----------------------------------------------------------------
#____________Error,failed...___________________________________
#____________LSINF1252___________________________________________
def error2(cursor):
    "nombre d'erreurs constatées dans les soumissions "
    values = []
    success = 0
    failed = 0
    timeout = 0
    overflow = 0
    error = 0
    for row in cursor.execute('''SELECT course,result FROM submissions WHERE course = "LSINF1252"'''):
        if row[1] == "success":
            success += 1
        if row[1] == "failed":
            failed += 1
        if row[1] == "timeout":
            timeout += 1
        if row[1] == "overflow":
            overflow += 1
        if row[1] == "error":
            error += 1
    values = [success,failed,timeout,overflow,error]
    return values

#----------------------------------------------------------------
#____________Error,failed...___________________________________
#____________"LSINF1101-PYTHON"___________________________________________

def error1(cursor):
    "nombre d'erreurs constatées dans les soumissions "
    values = []
    success = 0
    failed = 0
    timeout = 0
    overflow = 0
    error = 0
    for row in cursor.execute('''SELECT course,result FROM submissions WHERE course = "LSINF1101-PYTHON"'''):
        if row[1] == "success":
            success += 1
        if row[1] == "failed":
            failed += 1
        if row[1] == "timeout":
            timeout += 1
        if row[1] == "overflow":
            overflow += 1
        if row[1] == "error":
            error += 1
    values = [success,failed,timeout,overflow,error]
    return values

#----------------------------------------------------------------
#____________Error,failed...___________________________________
#____________"LSINF1101-PYTHON"___________________________________________

def error(cursor):
    "nombre d'erreurs constatées dans les soumissions "
    values = []
    success = 0
    failed = 0
    timeout = 0
    overflow = 0
    error = 0
    for row in cursor.execute('''SELECT course,result FROM submissions WHERE course = "LEPL1402"'''):
        if row[1] == "success":
            success += 1
        if row[1] == "failed":
            failed += 1
        if row[1] == "timeout":
            timeout += 1
        if row[1] == "overflow":
            overflow += 1
        if row[1] == "error":
            error += 1
    values = [success,failed,timeout,overflow,error]
    return values


def close(conn):
    conn.close()

def main_for_grade1101():
    """
        cette fonction doit retourner le resultat (une liste) du cours LSINF1101
    """
    cursor, conn = start()
    data1 = gradeforlsinf1101(cursor)
    close(conn)

    return data1


def main_for_grade1252():
    """
        cette fonction doit retourner le resultat (une liste) du cours LSINF1252
    """
    cursor, conn = start()
    data2 = gradeforlsinf1252(cursor)
    close(conn)

    return data2

def main_for_grade1402():
    """
        cette fonction doit retourner le resultat (une liste) du cours LEPL1402
    """
    cursor, conn = start()
    data3 = gradeforlepl1402(cursor)
    close(conn)

    return data3


def main_for_LSINF1101():
    """
        cette fonction doit retourner le resultat (une liste) du cours LSINF1101
    """
    cursor, conn = start()
    data4= LSINF1101(cursor)
    close(conn)

    return data4

def main_for_LSINF1252():
    """
        cette fonction doit retourner le resultat (une liste) du cours LSINF1252
    """
    cursor, conn = start()
    data5= LSINF1252(cursor)
    close(conn)

    return data5


def main_for_LEPL1402():
    """
        cette fonction doit retourner le resultat (une liste) du cours LEPL1402
    """
    cursor, conn = start()
    data6= LEPL1402(cursor)
    close(conn)

    return data6


def main_for_generalLSINF1252():
    """
        cette fonction doit retourner le resultat (une liste) du cours LSINF1252
    """
    cursor, conn = start()
    data7= generalLSINF1252(cursor)
    close(conn)

    return data7



def main_for_generalLSINF1101():
    """
        cette fonction doit retourner le resultat (une liste) du cours LSINF1101
    """
    cursor, conn = start()
    data8= generalLSINF1101(cursor)
    close(conn)

    return data8


def main_for_generalLEPL1402():
    """
        cette fonction doit retourner le resultat (une liste) du cours LEPL1402
    """
    cursor, conn = start()
    data9 = generalLEPL1402(cursor)
    close(conn)

    return data9

def main_for_error2():
    """
        cette fonction doit retourner le resultat (une liste) du cours LEPL1402
    """
    cursor, conn = start()
    data10 = error2(cursor)
    close(conn)

    return data10

def main_for_error1():
    """
        cette fonction doit retourner le resultat (une liste) du cours LSINF1101
    """
    cursor, conn = start()
    data11 = error1(cursor)
    close(conn)

    return data11

def main_for_error():
    """
        cette fonction doit retourner le resultat (une liste) du cours LSINF1252
    """
    cursor, conn = start()
    data12 = error(cursor)
    close(conn)

    return data12