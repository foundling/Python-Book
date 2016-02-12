import os

from flask import Flask, render_template, redirect
from flask.ext.misaka import Misaka

chapters = [
    'introduction',
    'iterables',
    'functions',
    'terminology'
]

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('toc.html', chapters=chapters)

@app.route('/ch/<int:id>')
def chapter(id):

    if id >= len(chapters) or id < 0:
        return redirect('/')

    chapter_path = 'templates/chapters/' + chapters[id] + '.md' 
    exercises_path = 'templates/chapters/' + chapters[id] + '_exercises' + '.md'

    links = {
        'next': {
          'id'   : (id + 1) % len(chapters),
          'name' : chapters[(id + 1) % len(chapters)]
        },
        'prev': {
          'id'   : (id - 1) % len(chapters),
          'name' : chapters[(id - 1) % len(chapters)]
        }
    } 

    content = open(chapter_path).read() if os.path.exists(chapter_path) else None
    exercises = open(exercises_path).read() if os.path.exists(exercises_path) else None 

    print exercises

    return render_template('chapters/chapter.html', content=content, exercises=exercises, links=links)

Misaka(app)
app.run(debug=True,host='0.0.0.0')
