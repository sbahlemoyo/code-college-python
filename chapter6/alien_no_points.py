alien = {
    'color': 'green',
    'speed': 'slow'
}
# #key error will be thrown
# print(alien['points'])

#adding points key
point_value = alien.get('points', 'No point value assigned')
print(point_value)