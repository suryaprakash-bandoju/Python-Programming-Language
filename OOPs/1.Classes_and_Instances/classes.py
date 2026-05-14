class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + last +"company@.com"
        
    def full_name(self):
        return f"{self.first}{self.last}"
        
emp1 = Employee("Surya", "Prakash", 600000)

print(emp1.email)
print(emp1.full_name())