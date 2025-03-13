# sandwich_orders = ['bacon', 'pastrami', 'ham', 'cheese', 'pastrami','avocado', 'egg', 'pastrami']
# finished_sandwiches = []
# print('Oh no, looks like we ran out of Pastrami')
# while sandwich_orders:
#     if 'pastrami' in sandwich_orders:
#      sandwich_orders.remove('pastrami')
#     else:
#      made_sandwich = sandwich_orders.pop(0)
#      finished_sandwiches.append(made_sandwich)
#      print(f'I made your {made_sandwich.title()} sandwich!\n')
    

# print('These are all the sandwiches that have been made:\n')
# for complete_order in finished_sandwiches:
#     print(f'\t{complete_order.title()}')

poll_results = {}
polling_active = True

while polling_active:
   poll_user = input('Enter your name')
   ask_dream_vacay = input('\nWhat is your dream vacation destination?')

   poll_results[poll_user] = ask_dream_vacay

   end_poll_question = input('Would you like to give someone else a try?(yes or no)')
   if end_poll_question == 'no':
      polling_active = False

print('----Poll Results----\n')
for user, result in poll_results.items():
   print(f'{user.title()} : {result.title()}')
   
   


   


