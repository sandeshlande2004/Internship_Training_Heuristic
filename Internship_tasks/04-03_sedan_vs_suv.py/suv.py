for row in range(7):
    for col in range(21):
        if (row == 0 and (col >=0 and col < 12))or\
            (row == 1 and (col == 0 or col == 12)) or\
            (row == 2 and (col == 0 or col == 13)) or\
            (row == 3 and (col == 0 or col > 13)) or\
            (row == 4 and (col == 0 or col == 20)) or\
            (row == 5 and (col == 0 or col == 20)) or\
            (row == 6 and (col >=0 and col < 21)):
            print("*", end= ' ')
        else:
            print(" ", end= ' ')
    print()