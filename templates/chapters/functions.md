# Functions

### What is a function?

There are special ways to create new things in a program.  One way is to use the `=` operator in  the example `a = 5`, which binds the value `5` to the name `a`. In other words, you're telling Python: 'when I write `a`, I expect to get 5'. Another way to create something new is to use the `def` keyword, which defines a function.  

    def my_function():
        #code goes here

But what exactly *is* a function? If you recall from mathematics, a function takes some input and transforms it, yielding some potentially new value. The whole thing is a bit mystical to think about.  Here's a mathematical function: 

    f(x) -> x^2

The things I want to draw attention to are practical: some `x` is sent into the function. The squared value of `x` is calculated and then sent out.

`x` is the **input**.

`x^2`, when evaluated with some numerical value of `x`, is the **output**.

Here's an analog in Python:

    def f(x):
        return x*x


However, you aren't required to have either inputs or return values.  You could write something like:

    def get_name():
        name = raw_input("Enter your name: ")
        print name

Some functions are useful for transforming input into output and returning it, like the function that takes in `x` and returns `x` squared. Others, like `get_name` are useful for interacting with parts of the system that are defined outside of the function. It is also possible for a function to do both things at once. But one drawback of functions that use data defined in remote locations is that they are less portable, harder to read and harder to be confident about. But this fact is inescapable to some degree. 

The `raw_input` function, as I just alluded to, is not defined inside of `get_name`, but somewhere else. Where is that? They are defined in the **runtime** environment. When does that happen? Before your program is executed (or if you're using the interpreter, before you're given a prompt to start typing Python code), a bunch of names and values are loaded into the program that you can use from anywhere in the program. Some of those names refer to `built-in` functions. 

Let's try out a common `built-in`:

    len()

Ah ha! This didn't work. Did you get this error message?

    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-2-a927e5264703> in <module>()
    ----> 1 print len()

    TypeError: len() takes exactly one argument (0 given)


Note the `TypeError`: 'len() takes exactly one argument(0 given)'.  What is an argument? An argument is a value written in between the parentheses of a function call.  Let's try again:

    len('test')

If you run this in the interpreter, it will print back 4. But if you run a script with just this, it will not print anything. The reason is that the interpreter's behavior is more for the purpose of interactive programming, so it is efficient to have the values printed when they are entered and evaluted. But a Python file won't print out the value by default. You should use `print` to do that.  

    print len('test')

An argument is some value that you pass to a function when you call it.

Calling a function is done by writing the name, followed by a set of parentheses that can contain from 0 to many argument names separated by commas:

    def f(a,b,c):
        # code goes here 

A note on arguments: they look like variable names, but since they are in the definition, they merely describe the form of the code to be run when the function is actually called, i.e., they are incomplete, value-wise, until you call the function `f` with three values.  At definition time, you are saying, 'if I call `f` with the proper number of arguments, I can access the first as `a`, the second as `b` and the third as `c` inside of `f`. 

So with `len`, we got that error because we needed to pass it a single *argument*.  If we passed it two, it would give us a similar error. Some languages might ignore any unused arguments to the function, but Python throws a `TypeError`.

### Functions inside of Functions ?!?!?!

Yes, that's right. Here's an example:

    def f():
        print 'I am function f'
        def g():
            print 'I am function g.'

    f()

Now for a quiz: What does the last line, `f()`, print?

<input type="radio" name="q1" value="first" />
<pre>I am function 'f'</pre>
<input type="radio" name="q1" value="second" />
<pre>I am function'f'<br>I am function 'g'</pre>


When you call f, you define `g`. But `g` isn't called, so `f()` just prints "I am function 'f'".

You could also do this:

    def f():
        print "I am function f"

    def g(some_func):
        print some_func()
    
    g()        

How many functions are called when this code runs?

<input type="radio" name="q1" value="1" />
<label>1</label>
<input type="radio" name="q1" value="2" />
<label>2</label>
<input type="radio" name="q1" value="3" />
<label>3</label>

This one is intentionally tricky, but what do you think `b(a)` prints?

def a(some_func):
    print 'I am a.'    
    some_func(b)

def b(some_other_func):
    some_other_func(a)

b(a)

If this confuses you, that only means that you are paying attention.  This is what is going on:

b is called on the value a, which is a function.
inside b, a (now called 'some_other_func') is called on a.
a prints 'i am a.' and then calls some_func (which is a) on the value b, a function.

b then calls ....

### Why use them?

1. Functions group together lines of code to be run together so you can conveniently treat all of those lines as **a single thing**.

Example:

    # get_username() is a handy way of acting in your program 
    # without having to keep all the details in your head!
    get_username()

2 This means you can write a function once but use it many times, saving yourself from a lot of repetition.

Example:

    # wow, this is a handy way of doing something over and over again without having to retype all of the nitty-gritty details!
    get_username()
    get_username()
    get_username()
    get_username()
    get_username()
    get_username()

- Functions aid the **problem-solving process**: if you break your problem into smaller tasks, you can solve each task in a separate function. If you give descriptive names to your functions (and variables), you will be able to read your code two weeks later. 

Example:

    # get a username, check if the user can login, and respond accordingly, depending on his or her authorization status
    user_name = get_username()
    is_authorized = is_user_authorized(user_name)
    notify_user(is_authorized)

### Some Basic Terminology

- You **call** a function in order to run the code contained inside of it. A function call includes a variable name and a set of `()` at the end. 
- A function can also accept **arguments** which are one or more some comma-separated names in inserted between the parentheses. These make values outside the function accessible to the functions inside.
- You define a function when you want to take some code and make it reusable

Example without using functions:

    # get the user's name and print it out in a nice way
    name = raw_input('what is your name?')
    print 'Hi, my name is', name, '.'

Example with a function:

    def get_name():
        name = raw_input('what is your name')
        print 'my name is', name

    get_name()


Now, imagine you might need to get a user's name multiple times. It would only take 3 times before using a function becomes more efficient than typing out the same thing again and again.

Let's say `N` is the number of times you want to get a user's name and print it. Here's a chart that shows you how many lines of code (`loc`) you've saved by using a function instead of repeatedly writing out the individual lines, as `N` increases.


     N  |  loc with get_name() | loc without get_name()
    --- | -------------------- | ----------------------
     1  |         4            |           2             
     2  |         5            |           4             
     3  |         6            |           6             
 
     ...

     10 |         13           |           20             

     ...

     20 |         23           |           40             


You may be thinking, "23 lines versus 40 lines isn't *that* much of a difference".  But if the code you want to run is 10 lines long, the table might look like this:

     N  |  loc with get_name() | loc without get_name()
    --- | -------------------- | ----------------------
     1  |         12           |           10             
     2  |         13           |           20             
     3  |         14           |           30             

     ...

     10 |         21           |           100             

     ...

     20 |         31           |           200             


The function that expresses the number of lines of code you're required to write when using a function is `(lines + 1) + N`, whereas without it it is `N * lines`. So, if you run `get_name()` just twice, you're already saving 7 lines of code over writing out the lines over again.  If you call the function 20 times, you're saving 169 lines of code.


