usernames = ['admin', 'jaden', 'sbahle', 'nomvula', 'zuko']

for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")

#no users
usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

#checking usernames
current_users = ['Admin', 'Jaden', 'Sbahle', 'Zuko', 'Thando']
new_users = ['thando', 'ZUKO', 'Anele', 'Lerato', 'Nina']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a new one.")
    else:
        print(f"Username '{new_user}' is available!")

#ordinal numbers
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

