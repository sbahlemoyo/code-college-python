banned_users = ['andrew', 'carolina', 'david']  # List of users who are banned
user = 'marie'                                  # Current user

if user not in banned_users:                    # Check if the user is not banned
    print(f"{user.title()}, you can post a response if you wish.")  # Allow the user
