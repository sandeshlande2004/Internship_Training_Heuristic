#normal print statement
print("Internship and Training by Heuristic")

#use of variables
a=10
print(a)

_var = 'India is a great nation'
print(_var)

# casesensitive
A='python'
print(A)

# overwrite variable
b=20
b='Nobita'
print(b)

# multiple variables
c,d,e=10,20,30
print(str(c)+str(d)+str(e)) #concatation of strings using + operator and str
print(c+d+e) #addition of numbers

#strings
str1 = 'Rohit'
str2 = 'Virat'
str3 = 'Sachin'
jno1 = 45
jno2 = 18
jno3 = 10
print(str1 + str2 + str3) #concatenation of strings ie addition
print(str1+ " " +str(jno1)) #concatenation of string and number
print(str2+ " " +str(jno2))
print(str3+ " " +str(jno3))

#slicing
string = "Python"
print(string)
print(string[0]) #indexing of string
print(string[:4])
print(string[3:])
print(string[0:4]) 
print(string[0:3:2]) #slicing with step
print(string[-1]) #negative indexing
print(string[-4:]) #negative slicing
print(string[-5:-2]) 

#datatypes

#integers
print(type(10))
a = 100 
print(type(a)) #type of variable
#float
b = 100.0
print(type(b))
#string
c = '100'
print(type(c))
#boolean (true or false)
d = True
print(type(d))
# complex number
e = 100+3j
print(type(e))

#array  Generally python dont have an array but we can use list as array
arr = [1,2,3,4,5]
print(arr)

#  ** LIST**
list = ['a',12, 'raghav', 45.99, 'true']
print(list)
print(list[0]) #indexing of list
print(list[1:3]) #slicing of list
list.append('new') #append new element to list
print(list)
list[2] = 'viraj' #overwrite element of list
print(list)
list.remove('true') #remove element from list
print(list)
list.pop() #remove last element from list
print(list)
list.pop(1) #remove element from specific index
print(list)
list.insert(1, 'new') #insert element at specific index
print(list)
list.reverse() #reverse the list
print(list)

list1 = [10,45,9,2,3,6,7,8,1]
list1.sort() #sort the list
print(list1)

print(list+list1) #concatenation of two lists

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

# **DICTONARY**

dict = {'name': 'M S Dhoni', 
        'age': 39, 
        'team': 'CSK', 
        'runs': 4500,
        'wickets': 0,
        'matches': 204}
print(dict)
print(dict['name']) #indexing of dictionary
print(dict['age'])
dict['wickets'] = 7 #overwrite the value of dictionary
print(dict)
print(dict.keys()) #keys of dictionary
print(dict.values()) #values of dictionary
print(dict.items()) #items of dictionary
print(dict.get('name')) #get the value of dictionary
dict.update({'team': 'MI'}) #update the value of dictionary
print(dict)
dict.pop('matches') #pop the value from dictionary
print(dict)
dict.popitem() #pop the last item from dictionary
print(dict)
dict.clear() #clear the dictionary
print(dict)

dict1 = {'name': 'Virat',
        'age': 32,
        'team': 'RCB',
        'runs': 5800,
        'wickets': 0,
        'matches': 180}
print(dict1)
print(dict.update(dict1)) #update the dictionary dict with dict1
print(dict)

# OPEARTORS

#aithematic operators
A = 10
B = 100
#addition
add = A + B
print(add)
print(A+B)
#substraction
sub = A - B
print(sub)
print(A-B)
print(B-A)
#multiplication
mul = A * B
print(mul)
print(A*B)
#division
div = A / B
print(div)
print(A/B)
print(B/A)
#modulus
mod = A % B
print(mod)
print(A%B)
print(B%A)
#exponential
exp = A ** B
print(exp)
print(A**B)
#floor division
floor = A // B
print(floor)
print(A//B)
print(B//A)

#assignment operators
a = 10
b = 20
a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b 
print(a)
a //= b 
print(a)
a %= b
print(a)
a **= b
print(a)

num = 5
num += 20
print(num)

#comparison operators
p = 50
q = 100
print(p == q)
print(p != q)
print(p > q)
print(p < q)
print(p >= q)
print(p <= q)

#logical operators
print('logical operators')
a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)

#identity operators
print('identity operators')
a = 10
b = 10
print(a is b)
print(a is not b)







