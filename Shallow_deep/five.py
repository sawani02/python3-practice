
# in deep copy address is copied values 
# are copied

from copy import copy

lst1 = ['a', 'b', 'c', 'd']
lst2 = copy(lst1)

lst2[3] = 's'

print lst2
print lst1