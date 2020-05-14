from flask import Flask, render_template, url_for, request, redirect, make_response
import sqlite3
import json
import functions

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

#------------------LSINF1252------------------------------------------------

@app.route('/LSINF1252')
def LSINF1252():
    """ Pour savoir ce qu'il fait voir function.py """
    return render_template('LSINF1252.html', content= functions.main_for_LSINF1252())


@app.route('/LSINF1252/porcentage')
def generalLSINF1252():
    """ Pour savoir ce qu'il fait voir function.py """
    return render_template('generalLSINF1252.html',content = functions.main_for_generalLSINF1252())

@app.route('/error2')
def error2():
    """ Pour savoir ce qu'il fait voir function.py """
    return render_template('error2.html',content= functions.main_for_error2())

@app.route('/grade1')
def fct_for_LSINF1252():
    """ Pour savoir ce qu'il fait voir function.py """ 
    return render_template('gradeLSINF1252.html', second= functions.main_for_grade1252())


#-----------------------LSINF1101----------------------------------------------------------

@app.route('/LSINF1101')
def LSINF1101():
    """ Pour savoir ce qu'il fait voir function.py """
    return render_template('LSINF1101.html', content= functions.main_for_LSINF1101() )


@app.route('/LSINF1101/pourcentage')
def generalLSINF1101():
    """ Pour savoir ce qu'il fait voir function.py """
    return render_template('generalLSINF1101.html',content = functions.main_for_generalLSINF1101())

@app.route('/error1')
def error1():
    """ Pour savoir ce qu'il fait voir function.py """
    return render_template('error1.html',content= functions.main_for_error1())

@app.route('/grade')
def fct_for_LSINF1101():
    """ Pour savoir ce qu'il fait voir function.py """
    return render_template('gradeLSINF1101.html', content= functions.main_for_grade1101())


#----------------------------LEPL1402-----------------------------------------------------------

@app.route('/LEPL1402')
def LEPL1402():
    return render_template('LEPL1402.html', content= functions.main_for_LEPL1402())


@app.route('/LEPL1402/porcentage')
def generalLEPL1402():

    return render_template('generalLEPL1402.html', content= functions.main_for_generalLEPL1402())

@app.route('/error')
def error():
    return render_template('error.html',content= functions.main_for_error())

@app.route('/grade2')
def fct_for_LEPL1402():
    """ Pour savoir ce qu'il fait voir function.py """
    return render_template('gradeLEPL1402.html', gear= functions.main_for_grade1402())
#---------------------------------------------------------------------------------------

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ ==  '__main__':
    app.run(debug=True)