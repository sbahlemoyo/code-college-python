class User():
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Age: {self.age}')
        print(f'Email: {self.email}')
    
    def greet_user(self):
        print(f'Welcome {self.first_name} {self.last_name}')
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'You have attempted to login {self.login_attempts} times.')

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privelages:
    def __init__(self):
        self.privelages = ['can add post', 'can delete post', 'can manage new and current users', 'can remove users']
        
    def show_privelages(self, person):
        print(f'Hey {person.first_name}, these are your admin privelages: ')
        for privelage in self.privelages:
            print(privelage.capitalize())
        

class Admin(User):
    """A specialised class for an admin user"""
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privelage = Privelages()