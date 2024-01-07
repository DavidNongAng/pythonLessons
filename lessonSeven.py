import math

print("It's math! It has type {}".format(type(math)))

# math is a module. A module is just a collection of variables defined by someone else.

print(dir(math))

print("pi to 4 significant digits = {:.4}".format(math.pi))

print(math.log(32, 2))

import math as mt  # rename it under a shorter alias to same typing

print(mt.pi)

from math import *

print(pi, log(32, 2))

import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
      )

rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)

# type() (what is this thing?)
type(rolls)

# dir() (what can I do with it?)
print(dir(rolls))

# If I want the average roll, the "mean" method looks promising...
rolls.mean()

# Or maybe I just want to turn the array into a list, in which case I can use "tolist"
rolls.tolist()

rolls + 10

# At which indices are the dice less than or equal to 3?
print(rolls <= 3)

xlist = [[1, 2, 3], [2, 4, 6],]
# Create a 2-dimensional array
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))

