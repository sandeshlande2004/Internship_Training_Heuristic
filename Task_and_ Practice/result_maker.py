title = 'PYTHON BASED RESULT MAKER' 
print(title.center(50, '*'))
print('------------------------------------------------------')
dev = 'Developed by: Er. Sandesh Lande'
print(dev.center(50))
print('------------------------------------------------------')
welcome = 'Welcome to the Python Based Result Maker'
print(welcome.center(50))
print('------------------------------------------------------')

eng = int(input('Enter English Marks: '))
math = int(input('Enter Maths Marks: '))
sci = int(input('Enter Science Marks: '))
sst = int(input('Enter Social Science Marks: '))
mar = int(input('Enter Marathi Marks: '))
print('------------------------------------------------------')

if(eng > 100 or math > 100 or sci > 100 or sst > 100 or mar > 100):
    print('Invalid Marks Entered')
    exit()

if(eng < 0 or math < 0 or sci < 0 or sst < 0 or mar < 0):
    print('Invalid Marks Entered')
    exit()
    
if(eng < 35 or math < 35 or sci < 35 or sst < 35 or mar < 35):
    print('You are Fail !!')
    print('Better luck next time')
    exit()
print('English: ', eng)
print('Maths: ', math)
print('Science: ', sci)
print('Social Science: ', sst)
print('Marathi: ', mar)
print('------------------------------------------------------')

total = eng + math + sci + sst + mar
print(f'Total marks {total} out of 500')
percentage = (total / 500)*100
print("------------------------------------------------------")
print('Total Percentage: ', percentage)
print('------------------------------------------------------')
if(percentage >= 75):
    print('Grade: Distinction')
elif(percentage >= 60):
    print('Grade: First Class')
elif(percentage >= 50):
    print('Grade: Second Class')
else:
    print('Grade: Pass')
print('------------------------------------------------------')

#using for loop
for _ in range(5):
    print("Congratulations !!")
    
# print('Congratulations'*10) #using mul operator

#using while loop
# count = 0
# while count < 5:
#     print("Congratulations !!")
