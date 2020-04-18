from flask import Flask, render_template,url_for,request,redirect, make_response
import sqlite3
import json

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')


@app.route('/LINF1252')
def LINF1252():
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
    return render_template('LINF1252.html', values=frecuencia, labels=cursos)


@app.route('/LINF1252/porcentage')
def genralLINF12():
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
    return render_template('genralLINF12.html', values=legend)
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


@app.route('/LSINF1101/porcentage')
def genralLINF11():
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
    return render_template('genralLINF11.html', values=legend)

#---------------------------------------------------------------------------------------

@app.route('/LPEPL1402')
def LPEPL1402():
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
    return render_template('LPEPL1402.html', values=frecuencia, labels=cursos)


@app.route('/LPEPL1402/porcentage')
def genralLEPL():
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
    return render_template('genralLEPL.html', values=legend)


if __name__ ==  '__main__':
    app.run(debug=True)