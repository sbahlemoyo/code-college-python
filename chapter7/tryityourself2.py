pizza_toppings = "Enter your choice of pizza topping."
pizza_toppings += "\nEnter 'quit' to end your order"

message = ""
while message != 'quit':
    message = input(pizza_toppings)
    message = message.lower().strip()
    if message == 'quit':
        break
    else:
        print(f'Adding {message.title()}...')


movie_age_query = 'Enter your age'
movie_age_query += '\nType \'exit\' to end your purchase'

active = True
while active:
    movie_age_query = input(movie_age_query)
    movie_age_query = int(movie_age_query)
    if movie_age_query != 'exit' and movie_age_query < 3 :
        print('Your ticket is free')
        active = False
    elif movie_age_query != 'exit' and movie_age_query >=3 and movie_age_query < 12:
        print('Your ticket is $10')
        active = False
    elif movie_age_query != 'exit' and movie_age_query >=12:
        print('Your ticket is $15')
        active = False
   
