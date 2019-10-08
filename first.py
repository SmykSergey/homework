from random import randrange
#buble
my_list = [ randrange(0, 15) for i in range(10) ]

max_list = len( my_list )

i = 0
while i < max_list:

    j = 0
    while j < max_list-i-1:

        if my_list[ j ] > my_list[ j + 1 ]:

            my_list[ j ], my_list[ j + 1] = my_list[ j + 1], my_list[ j ]
        j+=1
    i += 1

print( my_list )
