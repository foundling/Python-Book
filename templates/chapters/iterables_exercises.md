# Filtering Usernames 

For the following exercises, we are going to take a list of usernames and filter that list based on varying criteria.

Here's the list:

    usernames = [
        'redsoxfan9000', 
        'djcarl', 
        'donutman', 
        '?uestlove', 
        'bbgun', 
        'rjd2c3po', 
        'videogamez', 
        'lilly99'
    ]

Hint: you will find the for loop construct useful here, as well as using some data type to hold intermediate values during the loop. 

#### Ex. 0 - Upper Case 

Create a new list where each username is capitalized. Print the list.

## solution:
new_usernames = []
for name in usernames:
    capitalized_name = name.upper()
    new_usernames.append(capitalized_name)
print new_usernames
    
    

#### Ex. 1 - Six or Shorter

Go through the items in usernames and pick out the usernames that are 6 or less characters long. Put them in a new list and print that list.

#### Ex. 2 - Even Number of Characters 

Do the same as you did in the previous exercise, but only target the usernames that have an even number of characters. 

#### Ex. 3 - Total Characters

Find the total number of characters that the list of usernames contains. Print that number.

#### Ex. 4 - Comma Separated Aggregate of Usernames 

Create a string using the usernames list where each username is separated by a comma. Make sure that the last name has no trailing comma. Print that string.

#### Ex. 5 - Most Numbers in Username

Find the username(s) that contain the most numbers. 

#### Ex. 6 - Find the shortest username

#### Ex. 7 - Find the Longest username

#### Ex. 8 - Get a list of usernames that contain a 'z' or a non-alphabetic character.
