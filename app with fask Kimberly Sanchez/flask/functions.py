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
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
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
