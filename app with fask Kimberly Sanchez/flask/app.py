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
    print(frecuencia)
    for i in range(len(frecuencia)):
        values.append(frecuencia[i][0])
        cursos.append(frecuencia[i][1])
    return render_template('LSINF1252.html', values=values, labels=cursos)


@app.route('/LSINF1252/porcentage')
def generalLSINF1252():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
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
    for row in cursor.execute("SELECT course, submitted_on FROM submissions "):
        if row[0] == 'LSINF1252':
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

    return render_template('generalLSINF1252.html',values = values)

@app.route('/error2')
def error2():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
    values = []
    success = 0
    failed = 0
    timeout = 0
    overflow = 0
    error = 0
    for row in cursor.execute("SELECT course,result FROM submissions"):
        if row[0] == "LSINF1252" :
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
    values.append(success)
    values.append(failed)
    values.append(timeout)
    values.append(overflow)
    values.append(error)
    return render_template('error2.html',values = values)

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
        frecuencia.append((values.count(i),i))
    frecuencia = sorted(frecuencia)
    values = []
    cursos = []
    for i in range(len(frecuencia)):
        values.append(frecuencia[i][0])
        cursos.append(frecuencia[i][1])
    return render_template('LSINF1101.html', values=values, labels=cursos)


@app.route('/LSINF1101/pourcentage')
def generalLSINF1101():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
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
    for row in cursor.execute("SELECT course, submitted_on FROM submissions "):
        if row[0] == 'LSINF1101-PYTHON':
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

    return render_template('generalLSINF1101.html',values = values)

@app.route('/error1')
def error1():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
    values = []
    success = 0
    failed = 0
    timeout = 0
    overflow = 0
    error = 0
    for row in cursor.execute("SELECT course,result FROM submissions"):
        if row[0] == "LSINF1101-PYTHON" :
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
    values.append(success)
    values.append(failed)
    values.append(timeout)
    values.append(overflow)
    values.append(error)
    return render_template('error1.html',values = values)

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
        frecuencia.append((values.count(i),i))
    frecuencia = sorted(frecuencia)
    values = []
    cursos = []
    for i in range(len(frecuencia)):
        values.append(frecuencia[i][0])
        cursos.append(frecuencia[i][1])
    return render_template('LEPL1402.html', values=values, labels=cursos)


@app.route('/LEPL1402/porcentage')
def generalLEPL1402():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
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
    for row in cursor.execute("SELECT course, submitted_on FROM submissions "):
        if row[0] == 'LEPL1402':
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

    return render_template('generalLEPL1402.html',values = values)

@app.route('/error')
def error():
    conn = sqlite3.connect('inginious.sqlite')
    cursor = conn.cursor()
    values = []
    success = 0
    failed = 0
    timeout = 0
    overflow = 0
    error = 0
    for row in cursor.execute("SELECT course,result FROM submissions"):
        if row[0] == "LEPL1402" :
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
    values.append(success)
    values.append(failed)
    values.append(timeout)
    values.append(overflow)
    values.append(error)
    return render_template('error.html',values = values)

@app.route('/grade2')
def fct_for_LEPL1402():
    return render_template('gradeLEPL1402.html', gear= functions.main_for_grade1402())
#---------------------------------------------------------------------------------------

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ ==  '__main__':
    app.run(debug=True)