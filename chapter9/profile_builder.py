

class User:
    """Class that creates a user profile"""
    def __init__(self, f_name, l_name, age,gender,  email):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.gender = gender
        self.email = email

    def describe_user(self):
        """Displays information that describes user"""
        print(
            f"First Name: {self.first_name.title()}\nLast Name: {self.last_name.title()} \nAge: {self.age} \nGender: {self.gender.title()} \nEmail: {self.email}"
        )

    def greet_user(self):
        """Greets user"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}")

class Administrator(User):
    """Class that creates administrator profile"""

    def __init__(self, f_name, l_name, age, gender, email):
        super().__init__(f_name, l_name, age, gender, email)
        self.privelages = Privelages()   

class Privelages:
    """Class storing admin privelages"""
    def __init__(self):
        self.privelages = ["can add post", "can delete post", "can ban user", "can access user info"]
    
    def show_privelages(self):
        """shows admin privelages"""
        print("These are your privelages as an admin: \n")
        for privelage in self.privelages:
            print(f"{privelage.capitalize()}")      
