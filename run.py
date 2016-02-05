import os

from flask import Flask, render_template, redirect
from flask.ext.misaka import Misaka

chapters = [
    'introduction',
]

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('toc.html', chapters=chapters)

@app.route('/ch/<int:id>')
def chapter(id):

    if id >= len(chapters) or id < 0:
        return redirect('/')

    chapter_title = chapters[id] + '.md'  
    chapter_path = 'templates/chapters/' + chapter_title

    with open(chapter_path) as fh:
        content = fh.read()
        return render_template('chapters/chapter.html',content=content)

Misaka(app)
app.run(debug=True)
