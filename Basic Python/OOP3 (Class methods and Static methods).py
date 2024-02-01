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
    
        
    @classmethod
    def set_raise_amt(cls, amount): #cls is used for Class, in this case is Employee
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.slpit('-')
        return cls(first,last,pay)
    
    @staticmethod
    def is_workDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
# Regular methods pass the instance as the first argument
# classmethods pass the Class as the first argument
# static methods don't pass anything automatically
        
emp_1 = Employee('Anna', "Hyu", 50000)
emp_2 = Employee('Carl', 'Jacob', 60000)

# Same thing, but first one is used for the whole class, instead of one instance of the class.
Employee.set_raise_amt(1.05)
emp_1.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.email)
print(new_emp_1.pay)

# example static method
import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workDay(my_date))

