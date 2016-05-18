# Code Literacy

Why Read Code? 

Reading code sharpens your ability to think about a problem. Read it carefully but without fear. Code is human literature and says a lot about someone's intention. Due the to many layers of abstraction in an operating system, it's much more often the case that code is written for some other person than it is for a computer.  Understanding another's solution to a problem is edifying.

But reading code is scary.  Even if you know the language, the meaning of a project may be obscured by an unfamiliar or even bad style, a problem scale that you've never had to account for, or the density of detail required by the domain alone. Writing the best code is not easy to do and people have, accordingly, devised many solutions to this problem, many of which conflict. 

Nonetheless, there are some habits you can form to understand code more quickly and completely:

## Start at the main source file

It may be the case that you are reading a single-file project.  A lot of open-source library demos are in a single file, for example. These projects are likely not in a single file, though, so its important to know where to look.  Each programming community has its own variety of approaches to this, but in python if you see:

    if __name__ == '__main__':
        main()

you are in the top-level file that loids the code to run.

## Investigate just the function calls

Function calls are generally the agents of propulsion and duration in a program.  If you look at a program first as a series of function calls in their call order, its easier to see the story. Of course, some styles and approaches are more difficult than others.  For example, in asynchronous programming it is possible for the function call series to be determined by factors outside of your program environment. But ther are still rules.

