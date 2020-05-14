from flask import Flask, render_template, url_for, request, redirect, make_response
import sqlite3
import json
import functions


#_______________________________________________________________________
#----------------- Data LSINF1101---------------------------------------
#_______________________________________________________________________

@app.route('/LSINF1101')
def LSINF1101():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
    labels = []
    values = []
    cursos= []
    frecuencia = []
    for row in cursor.execute('''SELECT DISTINCT course, task, grade FROM submissions WHERE course = "LSINF1101-PYTHON"'''):
        if row[2] not in cursos:
            cursos.append(row[2])
    for row in cursor.execute('''SELECT DISTINCT course, task, grade FROM submissions WHERE course = "LSINF1101-PYTHON"'''):
            values.append(row[2])
    for i in cursos:
        frecuencia.append((values.count(i),i))
    frecuencia = sorted(frecuencia)
    values = []
    cursos = []
    for i in range(len(frecuencia)):
        values.append(frecuencia[i][0])
        cursos.append(frecuencia[i][1])
    return values=values, labels=cursos




#_______________________________________________________________________
#----------------- Data LSINF1252---------------------------------------
#_______________________________________________________________________


@app.route('/LSINF1252')
def LSINF1252():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
    values = []
    cursos= []
    frecuencia = []
    for row in cursor.execute("SELECT course,grade,task FROM submissions"):
        if row[0] == "LSINF1252" and row[2] not in cursos:
            cursos.append(row[2])
    for row in cursor.execute("SELECT course,grade,task FROM submissions"):
        if row[0] == "LSINF1252":
            values.append(row[2])
    for i in cursos:
        frecuencia.append((values.count(i),i))
    frecuencia = sorted(frecuencia)
    values = []
    cursos = []
    for i in range(len(frecuencia)):
        values.append(frecuencia[i][0])
        cursos.append(frecuencia[i][1])
    return render_template('LSINF1252.html', values=values, labels=cursos)
