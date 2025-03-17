import random
letters_and_num = [1, 'a', 5, 'd', 8, 'f', 0, 'l', 's', 2, 3, 4,7,9,6 ]
my_ticket = [2, 'a', 3, 'd']
attempts = 0  # Counts how many times we try
while True:
    attempts += 1  # Increment the attempt count
    drawn_ticket = random.sample(letters_and_num, 4)  # Pick 4 random elements
    if drawn_ticket == my_ticket:  # Check if we won
        print('Congratulations!You won')
        break  # Stop the loop if we have a match
print('The winning ticket was:')
print(drawn_ticket)
print(f"\nIt took {attempts} attempts to get a winning ticket!")






