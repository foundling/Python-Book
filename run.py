import os

from flask import Flask, render_template, redirect
from flask.ext.misaka import Misaka

chapters = [
    'introduction',
    'printing_values',
    'first_ data_ types',
    'iteration_basics',
]

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('toc.html', chapters=chapters)

@app.route('/ch/<int:id>')
def chapter(id):

    if id >= len(chapters) or id < 0:
        return redirect('/')

    title = chapters[id]
    template_file = ''.join([title,'.md']);  
    chapter_path = 'chapters/' + template_file
    return render_template(chapter_path)

Misaka(app)
app.run(debug=True)
