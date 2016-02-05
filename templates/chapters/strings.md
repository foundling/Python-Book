# Strings


## keywords 

+ index and bracket syntax
+ `len` function
+ slice syntax
+ reverse function

A string is a sequence of characters surrounded by quotes. Examples of strings:

````python
"python"
""
"abc"
"123"
"False"
````

In python, using 'single quotes' and "double quotes" are equivalent, so you can use whichever you like more. Just make sure to close a string with the same character with which you opened it. 

## Working with Strings

#### Exercise: Count `e`'s in a string

````python
# here's our string
animal = 'elephant'

count = 0
for letter in animal:
    if letter == 'e':
      count = count + 1

print "the word",animal, "has ", count, "e's."
````

#### Combine two strings

````python

salutation = 'Mr.'
last_name = 'Jones'
combined = salutation + ' ' + last_name 
print combined

````

#### Indexing into a string

You can think of a string as a composite datatype (a sequence of elements that occur in a particular order) where the name you use to refer to the string points to the beginning of the data. 

The index is how we refer to a specific element in the sequence.  Python provides us the bracket syntax `[n]` where `n` is distance in elements from the beginning of the data.   

````python

word = 'alpha'
print word[0] + word[1] + word[2] + word[3] + word[4]

````

Notice that `word[0]` prints the first character of `word`. This is because `word` itself is implicitly the start of the data that it points to. So, if we take our previous definition, then `0` is the distance from the beginning where we can find the first element, i.e. there is effectively no distance. 
