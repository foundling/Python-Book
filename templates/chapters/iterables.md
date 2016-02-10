# Sequences, Iterables and the `for` loop

A sequence is just a list of things in a particular order.

An **iterable** is a type of object in Python that lets you step through a sequence. Say your iterable is:

    letters = ['a','b','c'] 


Iterating through it will give you those values, `'A'`, `'B'`, `'C'`, one at a time. The way it works is you pick some mechanism for looping through things (for example, a `for` loop) as well as a single name for your iterator value. The code you specify runs for as many items are in the collection. Each time your code runs, it runs on a different element in the sequence and so the name you picked now refers to that next item. When there are no more items, the `for` loop knows internally to stop. 

Format: 

    for <iterator> in <iterable>:
        # code involving <iterator>, the value

Actual Code: 

    for <iterator> in <iterable>:
        # code involving <iterator>, the value

Calling it an 'iterable' indicates that you can use it in a particular *way*, so it is a bit more abstract because it doesn't express what it is, but how it behaves.

A sequence is a collection of values that exist in a particular order, where the values are not required to be unique. 

    # repeat elements are not a problem
    ['a','b','a']

Lots of things are sequences: names, dance routines, music, grocery lists.

One thing to note is that Python's method of iteration produces the *value* of the item as opposed to the value's position in the list. When it comes to the `for` loop, this is maybe surprising if you know other languages like C, Perl, JavaScript, Java, just to name a few, which are more index-focused. There is an idiomatic way to do this, though, involving the function `enumerate` within the `for` loop. For another time.

Here are some examples of iterables: 

    # a string
    'Mr. Jones'

    # a list
    [4,3,2,1]
 
#### Indexing: getting a value in a sequence

You might want to get a single value out of an iterable as opposed to the entire sequence. One way of doing this is to target this value by its index. Python follows the common convention of using 0-based indexes, so the first element of any sequence is 0. 

    name = 'Mr. Jones'
    print a[0]
    print a[1]
    print a[2]
    print a[3]
    print a[4]
    print a[5]
    print a[6]
    print a[7]
    print a[8]

This will print each letter on a separate line. It works fine, but a more reasonable way to do this would be to use a `for` loop:

    # prints 'name' as a single entity
    print name

    # prints name, letter by letter
    name = 'Mr. Jones'
    for letter in name:
        print letter

    # and a single character is also an iterable/sequence
    letter = name[0]
    letter[0]

Ready? 


    # these print the same thing
    print name[0]
    print letter

    print name[0][0]
    print name[0][0][0]
    print name[0][0][0][0]
    print name[0][0][0][0][0]
    print name[0][0][0][0][0][0]
    print name[0][0][0][0][0][0][0]
    print name[0][0][0][0][0][0][0][0]

    ...

So, a letter is infinitely indexible? It is.

  letter = 'a'
  while letter == 'a':
      letter = letter[0] 
