from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def index():
	return render_template("templates/map.html")

@application.route('/readme')
def about():
	return render_template("templates/about.html")

if __name__ == "__main__":
    application.run(debug=True)