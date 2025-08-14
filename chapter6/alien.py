alien_0 = {'color': 'green',
           'points': 5
           }

print(alien_0)

new_points = alien_0['points']
print(f'You just earned {new_points} points!')

#accessing values in a dictionary
print(alien_0['color'])
print(alien_0['points'])

#adding new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#starting with an empty dictionary 

alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 5

print(alien_1)

#modifying values in a dictionary
alien_1['color'] = 'yellow'
alien_1['points'] = 10
print(f'The alien is now {alien_1["color"]} and has a new point value of {alien_1['points']}.')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

print(alien_0['ship'])#an eror will be thrown because ship does not exist in our alien list



# #removing key-value pairs
# del alien_0['points']
# print(alien_0)



#Nesting
#making an empty list to add aliens to
aliens = []
#make 30 green aliens
for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow'
    }
    aliens.append(new_alien)

#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

#show how many aliens have been created
print(f'Total number of aliens: {len(aliens)}')

