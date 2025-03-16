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


user1 = User('sbahle', 'moyo', '24', 'dfgdghfj')
user2 = User('andre', 'myers', '34', 'sdfserhysrt')
user3 = User('tshepo', 'mokoena', '28', 'fgtghdh')

# user1.describe_user()
# user1.greet_user()
# user2.describe_user()
# user2.greet_user()
# user3.describe_user()
# user3.greet_user()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.reset_login_attempts()
# print(user1.login_attempts)

class Privelages:
    def __init__(self):
        self.privelages = ['can add post', 'can delete post', 'can manage new and current users', 'can remove users']
        
    def show_privelages(self, user):
        print(f'Hey {user.first_name}, these are your admin privelages: ')
        for privelage in self.privelages:
            print(privelage.capitalize())
        

class Admin(User):
    """A specialised class for an admin user"""
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privelage = Privelages()
        
admin = Admin('thabo', 'mokoena', '27', 'hjffdsdfcgfhj')

# admin.show_privelages()
# admin.privelage.show_privelages(admin)

            



