import sqlite3



connection = sqlite3.connect('uniguessur.db')
cursor = connection.cursor()




'''
create/ connect to db




Clues-------
id autoincrement primary
base 64 encoding of image
photo credit 
latitude 
longitiude
subjects Foreign Key


Subjects-------
clue id 
x
y
official name


Landmarks-----
offical name Primary Key
alternative names csv


Guess History-----
id primary auto increment
clue id
long
lat

############
Strip metadata,

center crop image to max aspect ratio of 2:1 or 1:2 (subject to change based on frontend).
scale image to max of 2000px per side.

open two windows, one for the image, one for answer map and subject answer .


'''




