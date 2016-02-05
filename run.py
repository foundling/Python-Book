from flask import Flask, render_template
from flask.ext.misaka import Misaka

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('python_exercises.md')

Misaka(app)
app.run(debug=True)
