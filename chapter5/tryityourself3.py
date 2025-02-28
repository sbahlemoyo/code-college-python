usernames = []
for user in usernames:
    print(f"Hello {user.title()} , welcome to our page!")

if 'admin' in usernames:
    print("Hello admin, would you like to see a status report?")
else:
    for user in usernames:
        print(f"Hello {user.title()}, thank you for logging in again.")

if usernames:
    for user in usernames:
        print({user})
else:
    print("We need to find more users!")

current_users = ["Ben", "Tessa", "May", "Cersei", "Jaime", "John"]
new_users = ["Naya", "Alexa", "Kate", "John", "Ben"]

for person in new_users:
    current_users2 = current_users[:]
    for current in current_users2:
        current.lower()
    if new_users in current_users2 :
        print("User already exists.Enter a new username.")
    else:
        print("Username available")

num = list(range(1,10))
for no in num:
    if no == 1:
        print(f'{no}st')
    elif no == 2:
        print(f'{no}nd')
    elif no == 3:
        print(f'{no}rd')
    else:
        print(f'{no}th')




    

