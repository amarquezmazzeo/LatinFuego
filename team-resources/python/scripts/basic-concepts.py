# Think of modules as a collection of related functions
from os import getcwd

where_am_I = getcwd() # Get the current working directory
print("Current working directory: " + where_am_I)

# Import the module you need, then access the attribute
import sys
print("Current platform: " + sys.platform) # Get your current system platform
print("Current Python version: " + sys.version) # Get Version of Python you are running

"""
There are several built in data structures
The list is a common data structure
Here is a variable called odds that is assigned a list of odd numbers
"""
odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

# Note: Python variables are dynamically assigned and the type does not need to be declared
from datetime import datetime
right_this_minute = datetime.today().minute
print("The current minute of the time is: " + str(right_this_minute))
# Demonstrates if and else. Also looks inside the odds variable that contains the list of odd numbers
if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute.")

from datetime import date
import calendar
today = date.today()
day_of_week = calendar.day_name[today.weekday()]
# Example shows the use of if, elif, and else
if day_of_week == 'Saturday':
        print("It's the weekend!")
elif day_of_week == 'Sunday':
        print("The weekend is almost over!")
else:
    print("Must be a work day!")





