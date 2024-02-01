#Magic/Dunder Methods

class Employee: 
    
    # Class variables
    raise_amount = 1.04
    
    # Constructor
    def __init__(self, first, last):
        #instance variables (or attributes)
        self.first = first
        self.last = last 
    
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    
emp_1 = Employee('Anna', "Hyu")

emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname