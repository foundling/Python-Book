from flask import Flask, render_template
from flask.ext.misaka import Misaka

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('toc.html')

@app.route('/ch/<id>')
def chapter(id):
    template = ''.join(['chapter_', id, '.md']);  
    return render_template(template)

Misaka(app)
app.run(debug=True)
