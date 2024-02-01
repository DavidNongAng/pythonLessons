#Magic/Dunder Methods

class Employee: 
    
    # Class variables
    raise_amount = 1.04
    
    # Constructor
    def __init__(self, first, last, pay):
        #instance variables (or attributes)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'    
    
    # Methods
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    # Used for debugging and logging
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    
    # Used as a display for the in user.
    def __str__(self):
        return '{} - {}'.format(self.fullName(), self.email)      
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullName())
    
emp_1 = Employee('Anna', "Hyu", 50000)
emp_2 = Employee('Carl', 'Jacob', 60000)

# print(emp_1)

print(repr(emp_1))
print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(int.__add__(1,2))
# print(str.__add__('a', 'b'))

print(emp_1 + emp_2)

print(len('test'))
print('test'.__len__())

print(len(emp_1))