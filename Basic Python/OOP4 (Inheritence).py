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
       

class Developer(Employee): #Sub class of Employee
    raise_amount = 1.10  
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay) # Passes the parameters to Employee constructor to let it handle instead of here.
        self.prog_lang = prog_lang
        
class Manager(Employee): #Sub class of Employee
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
 
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullName())
    
 
dev_1 = Developer('Anna', "Hyu", 50000, 'Java')
dev_2 = Developer('Carl', 'Jacob', 60000, "Ruby")

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

mgr_1 = Manager('Sue', "Smith", 90000, [dev_1])

# print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)

# mgr_1.print_emps()

# tells us if an object is an instance of a class
print(isinstance(mgr_1, Employee))
print(isinstance(Manager, Employee))
print(isinstance(Manager, Developer))

