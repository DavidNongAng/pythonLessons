# Introduction to Python

# Assigning value to variable.
spam_amount = 0
print(spam_amount)

# Reassigning the value
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

# type of variable
type(spam_amount)

a = 10
b = 5

# Math Operations
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # Floor division (Quotient of a and b, removing fractional parts. Rounded down)
print(a % b)
print(a ** b)  # Exponential

# Order of operations is PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction).

print(8-3+2)  # 7
print(-3 + 4 * 2)  # 5

hat_height_cm = 25
my_height_cm = 190

# How tall am I, in meters, when wearing my hat?
total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)

# Built-in Functions
print(min(1, 2, 3, 4, 5))
print(max(1, 2, 3, 4, 5))

print(abs(32))
print(abs(-32))

# 2 Main numerical types (int and float)
print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)

