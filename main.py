# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

secret_word = "goat"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter word: ")
        guess_count += 1
        if guess_count == 1:
            print("Hint: A mammal")
        elif guess_count == 2:
            print("Hint: Horned animal")

    else:
        out_of_guesses = True

if out_of_guesses:
    print("Sorry,You lose!")

else:
    print("You win")






class_mates = ["Jay", "Thad", "Ben", "Isaac", "Salim", "Ridwan", "Joel", "Aminu", "Laka"]


for names in range(len(class_mates)):
    print(class_mates[names])

# create an exponential function

def raise_to_power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result


print(raise_to_power(2, 10))


count = 1
while count <= 50:
    if count % 15 == 0:
        print("FizzBuzz")
    elif count % 5 == 0:
        print("Buzz")
    elif count % 3 == 0:
        print("Fizz")
    else:
        print(count)
    count += 1


"""
Write a short program that prints each number from 1 to 20 on a new line
For each multiple of 3, print "Fizz" instead of the number
For each multiple of 5, print "Buzz" instead of the number
For numbers which are multiples of both 3 and 5, print FizzBuzz instead of the number
"""

try:
    for number in range(int(input("Enter range of fizzbuzz: "))):
        if number == 0:
            print("\n")
        elif number % 15 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)
        number += 1

except ZeroDivisionError:
    print("invalid input")

# Calculate a running sum

sum_of_numbers = 1
enter_number = float(input("Enter a number"))
sum_of_numbers = sum_of_numbers + enter_number

if enter_number >= 0:
    print(sum_of_numbers)
    input("Enter another number: ")

else:
    print(sum_of_numbers)


#Ask the user to input their name and assign it to variable 'name'

#name = input('What is your name? ')
#print('Hello', name)

#Do math, ask user to input 2 numbers and store them in variables num1 and num2
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

sum = num1 + num2

print('The sum of numbers are: ', sum)


num3, num4 = input('Enter 2 numbers: ').split()
product = int(num3) * int(num4)
print(product)


print("Enter your favorite artists to perform; Enter 'q, to quit, 'r' to execute performance ")

artists = []

while True:
    artist_data = input()
    if artist_data == "q":
        print("Quitting program...")
        break
    elif artist_data == "r":
        print("{} is now performing".format(artists[0]))
        artists.pop(0)
    else:
        artists.append(artist_data)
        print(artists)

for item in artists:
    print("These artists are yet to perform: ", artists)

emails = {
    "Abe": "malgwiabraham@gmail.com",
    "Glory": "glorywilliamskamsy@gmail.com",
    "Wasabi": "was@gmail.com"
}
# if "Abe" in emails:
#     print(emails["Abe"])
# else:
#     print("No item found")

# for k, elem in emails.items():
#     print(k, elem)

story = """
The reverse method does not return anything so you cannot 
embed it in a print statement because the print function 
only prints out a return value. If you need to reverse a 
list or object without overwriting the original object, 
then making a copy and reassigning the original object is 
a good practice
"""


# conduits = ["and", "or", "not", "and", "not", "verb", "but", "verb", "because", "copy", "verb"]
#
# my_colors = {"blue", "white", "maroon", "black", "beige"}
# she_colors = {"lilac", "indigo", "maroon", "burgundy", "gold"}
#
# our_colors = my_colors - she_colors
# print(our_colors)

# We're going to create a dog class with 3 attributes and 3 characteristics.

class Dog():
    # class attributes of our dog
    gentle = True
    length = 15
    favorite = ["The Alchemist"]

    # here begins the attributes of our dog
    def __init__(self, name, colour, age):
        self.name = name
        self.colour = colour
        self.age = age

    # here ends the attributes of our doggo

    # here begins the capabilities of our dog
    def bark(self):

        print("{} is barking".format(self.name))

    def run(self):
        if self.age <= 20:
            print("{} is old, he can't run".format(self.name))
        else:
            print("{} is running.".format(self.name))

    def eat(self):
        print(f"{self.name} is having a treat")

    # here is the end of the capabilities of our dog


open("../input.txt", 'a')
file = open("../input.txt", 'a')

file.write("Are you my mama?\t33\n")
file.write("Just do it anyway.\t33")
file.close()

print("file frank sinatra")

import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()

c.execute('CREATE TABLE book (Title TEXT, Author TEXT, Pages INTEGER)')
# c.execute('INSERT INTO book VALUES ("Think Big", "Ben Carson", 100)')
# c.execute('INSERT INTO book VALUES ("Rich Dad, Poor Dad", "Robert Kiyosaki", 120)')

book = [
    ('Think Big', 'Ben Carson', 100),
    ('Rich Dad, Poor Dad', 'Robert Kiyosaki', 120),
    ('Think and Grow Rich', 'Napoleon Hill', 200)
]

c.executemany('INSERT INTO book VALUES (?,?,?)', book)
conn.commit()

c.execute('SELECT * FROM book WHERE Title="Think Big"')
data = c.fetchall()
print(data)

# """
# Problem: Receive miles and convert to kilometer
# Kilometers = Miles * 1.60934
# Enter 5 Kilometers
# Print the answer
# """
#
# miles = int(input("Enter miles you want to convert: "))
#
# kilometers = miles * 1.60934
#
# print("The distance is {}km" .format(kilometers))

# if age is 5, go to kindergarten
# Age 6 through to 17 goes to grade 1 through 12
# If 'a' is greater than 17, say go to college

age = eval(input("Enter your age: "))

if age == 5:
    print("Go to Kindergarten")

elif (age >= 6) and (age <= 17):
    print("Go to grade 1")

elif age > 17:
    print("Go to College")


# find odd numbers from 1 - 20

for number in range(1, 21):
    if not (number % 2 == 0):
        print("{} is odd".format(number))
    else:
        print(number)



