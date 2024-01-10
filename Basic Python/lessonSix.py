# Strings

x = 'Pluto is a planet'
y = 'Pluto is a planet'
print(x == y)


print("Pluto's a planet!")
print('My dog is named "Pluto"')
print('Pluto\'s a planet!')

hello = "hello\nworld"
print(hello)

triplequoted_hello = """hello
world"""
print(triplequoted_hello)
print(triplequoted_hello == hello)

print("hello", end='')
print("pluto", end='')

# Indexing
planet = 'Pluto'
print(planet[0])

# Slicing
print(planet[-3:])

# How long is this string?
len(planet)

# Yes, we can even loop over them
print([char+'! ' for char in planet])

# ALL CAPS
claim = "Pluto is a planet!"
claim.upper()

# all lowercase
claim.lower()

# Searching for the first index of a substring
claim.index('plan')

words = claim.split()
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')

'/'.join([month, day, year])

# Yes, we can put unicode characters right in our string literals :)
' 👏 '.join([word.upper() for word in words])

# Dictionaries
numbers = {'one': 1, 'two': 2, 'three': 3}

print(numbers)
numbers['eleven'] = 11
print(numbers)

numbers['one'] = 'Pluto'
print(numbers)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

print('Saturn' in planet_to_initial)

for k in numbers:
    print("{} = {}".format(k, numbers[k]))

# Get all the initials, sort them alphabetically, and put them in a space-separated string.
print(' '.join(sorted(planet_to_initial.values())))

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))


