# Overview of Terminology 

### Names

### Values

### Declaration and Definition 

### Evaluation

### Data

### Built-In Data Types

Representations of entities that you can use in your programs. Python makes the following data types available to you free of charge:

+ Integer 
+ Float 
+ Boolean 
+ String 
+ List
+ Object 
+ Dictionary 
+ Tuple 

Each of these have different purposes and demonstrate different behavior.

### Behavior

### Number

+ Integer

+ Float

+ Long 

+ Complex

### String

### Execution Order

The Python interpreter executes a file from top to bottom and from left to right. 

### Execution Model

This is a complex topic that you may want to do further research on if you decide you want to use Python seriously in the future.

### Boolean

A data type

### Function

### Call Stack

+ Function Definition

+ Function Call

### Return Value

### Module

### Class

### Object

### Property

### Method

### Scope

Assuming you've read the chapter about functions, we can talk about scope. A program can contain multiple uses of a name, but in different 'contexts'. The mechanism by which this is possible is called scope.  If you use a name somewhere in your program, the Python interpreter follows a method to determine what you meant (sometimes referred to as the LEGB rule), which figures out which value to use depending on where it is defined. It uses this process:

+ L: Is this name defined [l]ocally? If so, resolve this name to the value that is bound to that definition.
+ E: Is this name defined in an [e]nclosing function? If so, resolve this name to the value that is defined in the outer function's definition.
+ G: Is this name a [g]lobal variable? If so, ... you get the point.
+ B: Is this name a [b]uilt-in? If so, ... I hope you get the point.

Knowing something about the call stack and the Python runtime execution model will enrich your understanding of how scope works in Python, but you can work effectively with scope at first without this.  

Why is scope useful? Imagine a case where you weren't allowed to use the same name to refer to different values *anywhere* in your application (especially an application that involves multiple files).  You would have to resort to some tricky methods to refer to objects that don't need to be named differently. For example, say you have a function `square` and a function `square_root`:

````python
def square(num):
    # code goes here

def square_root(num):
    # code goes here
````

What if you had to make sure that the `num` in `square` didn't conflict with the `num` in `square_root` by renaming the latter to `num2` or `other_num` ? That would quickly become problematic if you build anything but a small  project. The LEGB rule for the scope mechanism makes things simpler: it looks within the function where `num` is first declared. If found, that is the one that is evaluated. If not, it keeps looking in the outside function according to a set of rules, yielding the name or an error if the name is ultimately not in scope. This way, if you write two functions and they are more or less independent of one another, you will never have to worry about naming conflicts. The two functions above, thanks to scope, are perfectly okay. 

Here's another example of Python's scoping mechanisms in action. 


    # define a function that prints a `num` and adds 10 to it
    def print_num():
        num = 10 
        print num

    num = 4
    print_num()
    print num



`print_num()` will output the value `10`. `print num` will output 4. Do you know why? Remember, what is important is where you see `num =` ..., or the location where num is defined.  Determining which function this declaration is in will help you make sense of scope.

In the case of `print_num()`, this is a function call so the program enters the `print_num` function and looks up the `num` there and finds `10`. In the case of `print num`, the num referred to is bound to the value 4 which is defined two lines above.

You might be wondering the difference between `print_num()` and `print num`.  For now, think of `print num` as something like `print(num)`. The first is a user-defined function and the second is a statement. The important thing here is that both access the value `num` and print the same value. 
