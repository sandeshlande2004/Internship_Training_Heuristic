# Bitwise operator

print('Bitwise operators')

#bitwise AND //Sets each bit to 1 if both bits are 1
print(5 & 3)  # 1

#bitwise OR //Sets each bit to 1 if one of two bits is 1
print(5 | 3)  # 7

#bitwise XOR //Sets each bit to 1 if only one of two bits is 1
print(5 ^ 3)  # 6

# bitwise NOT //Inverts all the bits
print(~5)  # -6

#bitwise left shift //Shift left by pushing zeros in from the right and let the leftmost bits fall off 
print(5 << 2)  # 20

#bitwise right shift //Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall
print(5 >> 2)  # 1
