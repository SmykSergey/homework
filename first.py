import random
import os
from random import randrange
from random import randint

"""
buble
my_list = [ randrange(0, 15) for i in range(10) ]

my_x_list = my_list
print( my_x_list )
max_list = len( my_x_list )

i = 0
while i < max_list:

    j = 0
    while j < max_list-i-1:

        if my_x_list[ j ] > my_x_list[ j + 1 ]:

            my_x_list[ j ], my_x_list[ j + 1] = my_x_list[ j + 1], my_x_list[ j ]
        j+=1
    i += 1

print( my_x_list)

"""

"""
a = [ {  i : random.randrange( 0, 999999999999999 ) }for i in range(1, 31 ) ]


print( a )

a = os.getcwd()
#a = os.path.exists(ai181.txt)
#print( a )
for a in os.listdir():
    print( a )
b = os.getcwd()
a = os.listdir( b )
#print( a )
create_my_file= open( '/home/serg/Desktop/ptrhon_algoritm/ai181.txt' , 'w' )
create_my_file.close()
"""

a = [ {  i : random.randrange( 0, 999999999999999 ) }for i in range(1, 31 ) ]

print( a )

with open('ai181.txt', 'w') as filehandle:
    for listitem in a:
        filehandle.write('%s' % listitem)

"""
a = ' '.join( a )
print( a )
my_file = open( '/home/serg/Desktop/ptrhon_algoritm/ai181.txt' , 'w'  )

my_file.write( a )
my_file.close()
y_file = open( '/home/serg/Desktop/ptrhon_algoritm/ai181.txt' , 'r+'  )
y_file = y_file.read()
print(y_file)
my_file.close()

"""





