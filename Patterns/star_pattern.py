# row = 5

# for i in range(row): #intially value of i is 0. So in op * will not print in 0th position
#     for j in range(i+1): #if we want to print * in 0th position we will increment i by 1 ie 0+1 = 1
#         print('*',end='')  #end ='' means don't print a new line after each print(). Print it on same line
#     print('') #this will print a new line after each iteration of i ie after one * next line then ** next line and so on

# for printing star pattern infinte time 
import time # time library to use time

i = 1
while True:  # Infinite loop
    print('*' * i)  # Print stars
    i += 1         # Increment the number of stars
    time.sleep(0.5)  # Add a delay of 0.5 seconds