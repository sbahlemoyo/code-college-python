class Employee():
    """A class containing everything about an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount = None):
        """Gives employee a raise"""
        if raise_amount:
            self.annual_salary += raise_amount
        else:
            self.annual_salary += 5000
        return self.annual_salary
