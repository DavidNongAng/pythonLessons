# Loops and list Comprehensions

# loop through a list
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ')  # print all on same line

# loop through a tuple
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print(product)

# loop through a string
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')

# range()
for i in range(5): # function that returns a sequence of numbers.
    print("Doing important work. i =", i)

#while Loops

i = 0
while i < 10:
    print(i, end=' ')
    i += 1
print()

# List comprehensions
squares = [n**2 for n in range(10)]
print(squares)

# without a list comprehension
squares = []
for n in range(10):
    squares.append(n**2)
print(squares)

short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

# str.upper() returns all all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)

# it could also be written as
loud_short_planets = [
    planet.upper() + '!'
    for planet in planets
    if len(planet) < 6
]

def count_negatives(nums):
    """Returns the number of negative numbers in the given list.

    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

def count_negative(nums):
    return len([num for num in nums if num < 0])



