tuple = (1, 2, 3, 4, 5, 'a','b','a')
print(tuple)
tuple_1 = tuple + (6, 7, 8) # This is how we can add new elements in tuple
print(tuple_1)
#for removing any element from tuple we can't use remove() method because tuple is immutable. For that we have to convert tuple into list and then we can remove any element from list.

my_list = list(tuple)
my_list.remove('a')
print(my_list)