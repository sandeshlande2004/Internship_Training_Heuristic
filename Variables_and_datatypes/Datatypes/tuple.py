tuple3 = (1, 2, 3, 4, 5, 'a','b','a')
print(tuple3)
tuple_1 = tuple3 + (6, 7, 8) # This is how we can add new elements in tuple
print(tuple_1)
#for removing any element from tuple we can't use remove() method because tuple is immutable. For that we have to convert tuple into list and then we can remove any element from list.

my_list = list(tuple3)
my_list.remove('a')
print(my_list)

# **TUPLE**
tuple = (1, 'a', 2, 'b', 3, 'c')
print(tuple)
print(tuple[0]) #indexing of tuple
print(tuple[1:3]) #slicing of tuple
#tuple[2] = 4 #tuple is immutable so we cant change the value of tuple

#tuple.append('new') #we cant append the value in tuple

#tuple.remove('a') #we cant remove the value from tuple

#tuple.pop() #we cant pop the value from tuple

#tuple.pop(1) #we cant pop the value from tuple

#tuple.insert(1, 'new') #we cant insert the value in tuple

#tuple.reverse() #we cant reverse the tuple

#tuple.sort() #we cant sort the tuple
tuple1 = (10,45,9,2,3,6,7,8,1)
print(tuple+tuple1) #concatenation of two tuples