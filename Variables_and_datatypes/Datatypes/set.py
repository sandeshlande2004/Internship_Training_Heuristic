set3 = {'a', 'b', 'c', 'd', 'e'}
print(set3)

set3.add('f') # To add any new element in set
print(set3)

set3.remove('a') # To remove any element from set
print(set3)

# **SET**
set = {'apple','mango', 'banana','pineapple' }
print(set)
# print(set[0]) #indexing of set is not possible
# print(set[1:3]) #slicing of set is not possible
# set[2] = 'new' #set is mutable so we cant change the value of
# set.append('new') #we cant append the value in set
# set.remove('apple') #we cant remove the value from set
# set.pop() #we cant pop the value from set
# set.pop(1) #we cant pop the value from set
# set.insert(1, 'new') #we cant insert the value in set
# set.reverse() #we cant reverse the set
# set.sort() #we cant sort the set
set.add('custard apple') #we can add the value in set
print(set)
set1 = {'sunflower','lily','mariegold','rose','lotus'}
print(set.union(set1)) #union of two sets
print(set.intersection(set1)) #intersection of two sets
print(set.difference(set1)) #difference of two sets
print(set.symmetric_difference(set1)) #symmetric difference of two sets