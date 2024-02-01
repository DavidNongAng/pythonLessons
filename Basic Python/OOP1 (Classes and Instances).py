# Python Object-Oriented Programming

class Employee: 
    
    # Constructor
    def __init__(self, first, last, pay):
        
        #instance variables (or attributes)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        
    def fullName(self):
        print('{} {}'.format(self.first,self.last))
        
    
emp_1 = Employee('Anna', "Hyu", 50000)
emp_2 = Employee('Carl', 'Jacob', 60000)

# display same thing.
print(emp_1.fullName())
print(Employee.fullName(emp_1))

