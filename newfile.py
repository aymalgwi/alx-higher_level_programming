# find odd numbers from 1 - 20

for number in range(1, 21):
    if not (number % 2 == 0):
        print("{} is odd".format(number))
    else:
        print(number)