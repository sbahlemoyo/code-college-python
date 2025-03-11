usernames = ["kate", "Sam", "Admin", "Erica", "Bruce"]
for user in usernames:
    if user.title() == "admin":
     print(f"Hello {user.title()}, would you like to see a status report?")
    else:
      print(f"Hello {user.title()} , welcome to our page!")

if usernames:
    for user in usernames:
        print(user)
else:
    print("We need to find more users!")

current_users = ["ben", "tessa", "may", "cersei", "jaime", "john"]
new_users = ["Naya", "Alexa", "Kate", "John", "Ben"]
#AskDavid
for new_user in new_users:
    new_user.lower()
    if new_user in current_users:
        print("Username already exists. Enter new username")
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




    

