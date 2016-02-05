{% extends "chapters/chapter_base.html" %}

{% block styles %}
  {% include "styles/chapter_styles.html" %}
{% endblock %}

{% block content %}
{% filter markdown %}
# For Loops

#### Terminology

ITERABLE:

an object that is made up of a sequence of values that you can go through, one at a time.  

example: 'abcde'
example: [1,2,3,4]

FOR LOOP:

one 'control construct' that python provides you with in order to go through an iterable, item by item. There are more ways to iterate through an iterable. 

form: 

for <temporary variable> in <iterable>:
    <code>

a for loop example:

    nums = [1,2,3,4]
    for n in nums:
    print n

another for loop example:

    name = 'bob'
    for l in name:
        print l
{% endfilter %}
{% endblock %}

{% block footer %}
  <a href="/">home</a>
{% endblock %}

{% block scripts %}
  {% include "scripts/chapter_scripts.html" %}
{% endblock %}
