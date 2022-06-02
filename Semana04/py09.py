""" #import my_module as mm
#from my_module import *
from my_module import find_index, test
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']

#index = mm.find_index(courses, 'Math')
index = find_index(courses, 'Math')
#print(index)
#print(test)

print(sys.path) """

import random
import math
import datetime
import calendar
import os
import antigravity

courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choice(courses)
rads = math.radians(90)
today = datetime.date.today()


print(random_course)
print(rads)
print(math.sin(rads))
print(today)
print(calendar.isleap(2020))
print(os.getcwd())
print(os.__file__)