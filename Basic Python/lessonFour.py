# Lists

primes = [2, 3, 5, 7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'],
]
# It can also be written ...

hand = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

my_favorite_things = [32, 'raindrops on roses', help]

print(planets[0])
print(planets[1])
print(planets[-1])
print(planets[-2])

# Slicing
print(planets[0:3])
print(planets[:3])  # ['Mercury', 'Venus', 'Earth']
print(planets[3:])  # ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets[1:-1])  # ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']
print(planets[-3:])  # ['Saturn', 'Uranus', 'Neptune']

# Changing lists

planets[3] = 'Malacandra'
print(planets)

planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)

# List Functions
len(planets)  # gives the length
sorted(planets)  # returns a sorted version of the list (alphabetical order)
sum(primes)  # adds all values.
max(primes)  # max value.

x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)

print(x.bit_length())

# Lists methods
planets.append('Pluto')  # modifies a list by adding an item to the end.
planets.pop()  # removes and returns the last element of the list
planets.index('Ur')  # gets the index of the element.
print("Ur" in planets)  # determine whether a list contains a particular value.
print("Calbefraques" in planets)

# Tuples

t = (1, 2, 3)  # or t = 1, 2, 3
# They cannot be modified (immutable)
