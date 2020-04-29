from flask import Flask, render_template, url_for, request, redirect, make_response
import sqlite3
import json
import functions

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')


@app.route('/LSINF1252')
def LSINF1252():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
    legend = 'Monthly Data'
    labels = []
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
        frecuencia.append(values.count(i))
    return render_template('LSINF1252.html', values=frecuencia, labels=cursos)


@app.route('/LSINF1252/porcentage')
def generalLSINF1252():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
    legend = []
    values = []
    succes = 0
    fail = 0
    for row in cursor.execute("SELECT course,grade,task FROM submissions"):
        if row[0] == "LSINF1252":
            values.append(row[1])
    for i in range(len(values)):
        if values[i] == 100.0:
            succes += 1
        else:
            fail += 1
    legend.append((succes * 100 )//(len(values)))
    legend.append(100- ((succes * 100 )//(len(values))))
    return render_template('generalLSINF1252.html', values=legend)

@app.route('/grade1')
def fct_for_LSINF1252():
    return render_template('gradeLSINF1252.html', second= functions.main_for_grade1252())
#---------------------------------------------------------------------------------

@app.route('/LSINF1101')
def LSINF1101():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
    legend = 'Monthly Data'
    labels = []
    values = []
    cursos= []
    frecuencia = []
    for row in cursor.execute("SELECT course,grade,task FROM submissions"):
        if row[0] == "LSINF1101-PYTHON" and row[2] not in cursos:
            cursos.append(row[2])
    for row in cursor.execute("SELECT course,grade,task FROM submissions"):
        if row[0] == "LSINF1101-PYTHON":
            values.append(row[2])
    for i in cursos:
        frecuencia.append(values.count(i))
    return render_template('LSINF1101.html', values=frecuencia, labels=cursos)


@app.route('/LSINF1101/pourcentage')
def generalLSINF1101():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
    legend = []
    values = []
    succes = 0
    fail = 0
    for row in cursor.execute("SELECT course,grade,task FROM submissions"):
        if row[0] == "LSINF1101-PYTHON":
            values.append(row[1])
    for i in range(len(values)):
        if values[i] == 100.0:
            succes += 1
        else:
            fail += 1
    legend.append((succes * 100 )//(len(values)))
    legend.append(100- ((succes * 100 )//(len(values))))
    return render_template('generalLSINF1101.html', values=legend)

@app.route('/grade')
def fct_for_LSINF1101():
    return render_template('gradeLSINF1101.html', content= functions.main_for_grade1101())


#---------------------------------------------------------------------------------------

@app.route('/LEPL1402')
def LEPL1402():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
    legend = 'Monthly Data'
    labels = []
    values = []
    cursos= []
    frecuencia = []
    for row in cursor.execute("SELECT course,grade,task FROM submissions"):
        if row[0] == "LEPL1402" and row[2] not in cursos:
            cursos.append(row[2])
    for row in cursor.execute("SELECT course,grade,task FROM submissions"):
        if row[0] == "LEPL1402":
            values.append(row[2])
    for i in cursos:
        frecuencia.append(values.count(i))
    return render_template('LEPL1402.html', values=frecuencia, labels=cursos)


@app.route('/LEPL1402/porcentage')
def generalLEPL1402():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
    legend = []
    values = []
    succes = 0
    fail = 0
    for row in cursor.execute("SELECT course,grade,task FROM submissions"):
        if row[0] == "LEPL1402":
            values.append(row[1])
    for i in range(len(values)):
        if values[i] == 100.0:
            succes += 1
        else:
            fail += 1
    legend.append((succes * 100 )//(len(values)))
    legend.append(100- ((succes * 100 )//(len(values))))
    return render_template('generalLEPL1402.html', values=legend)

@app.route('/grade2')
def fct_for_LEPL1402():
    return render_template('gradeLEPL1402.html', gear= functions.main_for_grade1402())
#---------------------------------------------------------------------------------------

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ ==  '__main__':
    app.run(debug=True)