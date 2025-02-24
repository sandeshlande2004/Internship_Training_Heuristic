print("While Loop")

#code for table of 2
# a = 1
# while(1):
#     if a <= 10:
#         table = 2*a
#         print(f"2 * {a} = {table}")
#         a += 1
        
#code for table of any number
no = int(input("Enter a number for table: "))
init = 1

while True:
    if init <= 10:
        result = no * init
        print(f"{no} * {init} = {result}")
        init += 1
