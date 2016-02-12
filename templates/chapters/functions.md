# Functions

### What is a function?

There are special ways to create new things in a program.  One way is to use the `=` operator in  the example `a = 5`, which says 'when i reference `a`, give me 5'. Another is to use the `def` keyword, which defines a function.  But what exactly *is* a function? If we recall from mathematics, a function takes some input and conceptually transforms it, yielding some output. The whole thing is a bit mystical to think about.  Here's the mathematical form: 

    f(x) -> x^2

The thing I want to draw attention to is the fact that `x` is sent into the function, but the expression to the right of the arrow describes what is sent out.

The closest analog in Python to the equation above would be this:

    def f(x):
        return x*x

`x` is the **input**.

`x^2` is the **output**.

However, you aren't required to have either inputs or return values.  You could write something like:

    def f():
        # open a file and read its contents into a string called content
        content = open('file.txt').read() 
        # print that string
        print content

Here, there are no arguments and there is no return value.

One thing to take away is that the input value `x` is being turned into `x^2`.  This is a `return` value.  You need to use the reserved word `return` in Python or the function will return a value you don't want. 

But not every function needs to return anything. If the 

So the equation says 'f is a function that when given a value yields that value squared'.


### Functions in Action

When you start up a Python interpreter or run a Python script, you are invoking the Python runtime environment (see the Runtime Environment chapter), which among other things gives you access to a bunch of highly useful pre-written in functions, referred to as `built-in`s. You can use a `built-in` just by writing out its name and appending `()` to the end. Here's an example: 

    print len()

This didn't work. Did you get this error message?

    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-2-a927e5264703> in <module>()
    ----> 1 print len()

    TypeError: len() takes exactly one argument (0 given)


That's right, 'len() takes exactly one argument(0 given)'.  If we look at our code again,

    print len()

An argument is some value that you give a function and ask it to use in a computation. It fits between the parentheses in `len()`. 

we need to pass the function an *argument*.  After all, we're calling a function `len`, but we didn't say *what* to get the length of.



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

- You **call** a function in order use the function. A function call includes a variable name and a set of `()` at the end. 
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


