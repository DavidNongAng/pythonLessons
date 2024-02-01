class Employee: 
    
    # Class variables
    num_of_emps = 0
    raise_amount = 1.04
    
    # Constructor
    def __init__(self, first, last, pay):
        #instance variables (or attributes)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'    
        
        Employee.num_of_emps += 1
    
    # Methods
    def fullName(self):
        print('{} {}'.format(self.first,self.last))
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
        
emp_1 = Employee('Anna', "Hyu", 50000)
emp_2 = Employee('Carl', 'Jacob', 60000)

emp_1.raise_amount = 1.05

print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)