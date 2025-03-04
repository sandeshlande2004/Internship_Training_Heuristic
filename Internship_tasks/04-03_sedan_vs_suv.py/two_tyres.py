for row in range(3):
    for col in range(21):
        if (row == 0 and (col == 3 or col == 7 or col == 13 or col == 17)) or\
            (row == 1 and (col > 3 and col < 7 or col > 13 and col < 17)):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()