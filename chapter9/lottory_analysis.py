from random import choice
letters_and_num = [1, 'a', 5, 'd', 8, 'f', 0, 'l', 's', ]
my_ticket = {'s': 'a'}
combo = f'{choice(letters_and_num)}{choice(letters_and_num)}'

tries = 1
while my_ticket:
    for i, v in my_ticket.items():
      if i and v in combo:
        print('Congratulations!You have the winning ticket')
        break
      else:
        print('Better luck next time!')
        tries +=1

print(f'It took you {tries} tries to finally win.')





