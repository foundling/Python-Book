# Iterables

An **iterable** is a type of object in Python that supports efficient traversal through its values in **sequential** order. If the iterable contains, say, 'a', 'b', and 'c', in that order, iterating through it will give you those values, one at a time. The way it works is you pick a single name for the value and each time you iterate to the next item, the name you picked now refers to that next item. 

You can think of an iterable as a piece of data that contains a collection of individual values in a specific order, where the values are not required to be unique. 

One thing to note is that Python's method of iteration produces the *value* of the item as opposed to the value's position in the list.  This is not the case in languages like C, JavaScript, Java, just to name a few. 

Here are some examples of iterables: 

    # a string
    'Mr. Jones'

    # a list
    [4,3,2,1]
 
#### Indexing: getting a value in a sequence

You might want to get a single value out of an iterable as opposed to the entire sequence. One way of doing this is to target this value by its index (note the first value has an index of 0, more on this soon). 

    a = 'Mr. Jones'
    print a[0]
    print a[1]
    print a[2]
    print a[3]
    print a[4]
    print a[5]
    print a[6]
