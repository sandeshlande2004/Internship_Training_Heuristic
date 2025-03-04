for row in range(3):
    for col in range(21):
        if (row == 0 and (col == 1 or col == 4 or col == 5 or col == 9 or col == 10 or col == 14 or col == 15 or col == 19)) or\
            (row == 1 and (col > 1 and col < 4 or col > 5 and col < 9 or col > 10 and col < 14 or col > 15 and col < 19)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()