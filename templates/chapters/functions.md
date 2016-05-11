# Functions

### What is a function?

There are special ways to create new objects in a program.  One way is to assign a value to a name using the `=` operator. Another way is to use the `def` keyword. `def` defines a function and the argument(s) it takes.   

    def my_function(arg1):
        print('I am a function with one argument {}: '.format(arg1)) 

But what exactly *is* a function? A heavy question. Let's not talk about that just yet. 

How is a function used? Well, the code above is demonstrating part of that process, namely the definition state of a function. That happens first and once per unique function. But what follows is the function call.

    my_function('Al was here!')

If you recall from mathematics, a function expresses a relationship between some range of inputs and their outputs. Here is a mathematical function: 

    f(x) -> x^2 | x e R

I would read this from left to right to mean: 'Here is some function `f` that when you give it `x`, e.g. `f(x)`, outputs `x` to the 2nd power. The `| x e R` just stipulates 'for all Real numbers', or as they say, '... such that x is a member of the set of all Real numbers'.

Here's an analogue in Python:

    def f(x):
        return x*x

There is an enormous difference between first mathematical function and the second more procedural function. You don't need to dig into the mathematical function to write a program.  However, the math determines the spectrum of data that function can take in the second function.

In Python, we use `def` to indicate that we are defining a function.  We name the function and provide a set of parentheses containing any arguments to it. Arguments aren't required, but the program will halt if it expects an argument when you've called it without one.  

The code contained in the function is always indented by a baseline number of spaces to the right (4 spaces is an okay indentation size) of each of the function's lines of code in the source text.


But you can also do *this* in Python:

    def f():
        ''' No args. No return value. No nothing '''

Or *this*:

    def no_op(): pass

### Return Values

As they say, a function called is a value returned. So you can think of a function (... a *synchronous* function, at least) as a stand-in for its returned value when reading the source text.

You might conceivably write something like this:

    def get_name():
        name = raw_input("Enter your name: ")
        print name
        # something is missing here

This is fine, it prints some input provided by the user. But its missing something that would make it more useful.  A `return` value. 

    def get_name():
        name = raw_input("Enter your name: ")
        # print(name)
        return name

This is better because another function can use its return value.

    # get the length of a username.
    # must 
    username = len(get_name())

I'm going to introduce some complications to the story now.  We returned a value but didn't take one in as an argument. What happened to input and output?  So where did `raw_input` come from? Well, it's a binding to a lower level region of the system that can fetch the keyboard input. Objects like these are generally included in a language's standard library. And this function is not passed in as an argument because it is not necessary to.

The fact is, we use a platform of tools to write programs, not merely a pure programming language.

Some functions are useful for transforming input into output and returning it, like the function that takes in `x` and returns `x` squared. Others, like `get_name` are useful for interacting with parts of the system that are defined outside of a given function but referenced inside of it. A function like this doesn't provide a return value, so here the analogy to math on the data level breaks down totally. But it is practical.  It is instruction-based. It is also possible for a function with both input values and a return value to change things defined elsewhere. 

Be aware that a major advantage to writing functions with only explicit arguments is that it is much easier to be certain about their results ( and to test that your conclusions are true ).


#### Built-ins

Above, I used the `raw_input` function inside of `get_name` but it was defined somewhere else. This is the sort of mysteriousness that I just referred to, but a `built-in`, such as `raw_input`, is part of the Python standard library, a collection of essential and useful tools for general use. We need to access these somehow.  These are bindings between names and values in the global namespace. We'll talk more about namespacing, but for now you can consider it to be similar to bookkeeping. 

Where does the standard library come from? It is loaded into the **runtime** environment before your program is executed. Or if you're using the interpreter, before you're given a prompt to start typing Python code), and some initialization, including the loading of a set of `built-in` modules like `len`, `raw_input` and `max`. Built-ins are loaded into the program and you can use them anywhere. 

Let's try out `len`:

    len()

Ah ha! This didn't work. Did you get this error message?

    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-2-a927e5264703> in <module>()
    ----> 1 print len()

    TypeError: len() takes exactly one argument (0 given)


It pays to learn to read these things.  I Always gravitate toward the line number and the type that TypeError specifies. It pays to learn type errors (you should see a lot of them). Here, note the `TypeError`: 'len() takes exactly one argument(0 given)'.  Well, what is an argument? It's the value in between the parentheses.  Let's try again:

    len('test')

There we go, a value back.  It prints print back 4. But if you run it as a script, it will not print anything. The reason is this: the interpreter evaluates code whenever you hit enter.  So it both promotes line by line experimentation and makes doing otherwise very difficult. Values are printed on evaluation because it saves you from having to constantly type 'print x'.  It's a free print statement everytime you press enter. Also, if you aren't sure what evaluation means, open up a Python terminal and try to find the smallest symbol you can type and not get an error after hitting Enter.  Any time the interpreter prints a value to you, that's evaluation. 

Anyway, a Python file won't print out the value when you're running a Python program. Yo need to use `print` to do that.  

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
    print 'A, here!'    
    some_func(b)

def b(some_func):
    some_func(a)

b(a)


Of course, programming isn't about solving the problem by going first to your keyboard.  Anything important *requires* time away from a computer.  It's a decision.  You want to be able to consider the essential things without distraction.  

You can minimize distraction by 'stubbing' out functions.  Here is an example:

    def newtonian_square_root(x):
        pass

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


