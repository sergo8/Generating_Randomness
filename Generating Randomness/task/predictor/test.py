import random

check = ["000", "001", "010", "011", "100", "101", "110", "111"]

string = '123456789'

for i in range(len(string)-3):
    print(string[0+i:3+i])


print(random.choices(['0', '1'], (4, 4)))