# Iterables

An iterable is a type of object in Python that supports efficient traversal through its values. In other words, you examine each of its values, one by one, in order. You can think of an iterable as a sequence, meaning that it is a collection of individual values in a specific order, where the values are not required to be unique. I'll use 'iterable' and 'sequence' interchangeably most of the time, but in contexts where their differences matter, I'll point out why.

Here are some examples of iterables: 

'Mr. Jones'

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
