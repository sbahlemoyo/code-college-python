from random import choice
letters_and_num = [1, 'a', 5, 'd', 8, 'f', 0, 'l', 's', 4, 2, 6, 3, 9, 7]

print('The following tickets have won a prize: ')
for i in range(0, 4):
    print(choice(letters_and_num))

