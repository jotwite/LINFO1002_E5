from flask import Flask
app = Flask(__name__)
from coronamenu import*

@app.route('/')
def index():
    """
    retourne le contenu de la page index.html
    """
    return coronamenu
'<!-- contenu de index.html ...'

@app.route('/page.html')
def page():
    """
    retourne le contenu de la page page.html
    """
    return contacts.html
'<!-- contenu de page.html ...'