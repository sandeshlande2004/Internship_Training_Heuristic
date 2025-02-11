print('If-elif-else loop')

user_age = int(input('Enter your age: '))

if(user_age <= 0):
    print('Invalid age')
elif(user_age >0 and user_age <= 12):
    print('You are a child')
elif(user_age > 12 and user_age <=18):
    print('You are a teenager')
elif(user_age > 18 and user_age <= 60):
    print('You are an adult')
else:
    print('You are a senior citizen')