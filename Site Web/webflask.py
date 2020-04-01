from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route("/coronamenu.html")
def home():
	return render_template("coronamenu.html")

@app.route("/coronaweb.html")
def web():
	return render_template("coronaweb.html")

@app.route("/coronacases1.html")
def confirmed():
	return render_template("coronacases1.html")

@app.route("/coronacases2.html")
def death():
	return render_template("coronacases2.html")

@app.route("/contacts.html")	
def contacts():
	return render_template("contacts.html")


if __name__== "__main__":
	app.run(debug=True)
