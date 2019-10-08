from random import randrange
import time
from datetime import datetime

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



from datetime import datetime
start_time = datetime.now()
# do your work here
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))