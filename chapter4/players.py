players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])#takes data from the beginning to the (4-1) index.
print(players[2:])#prints from the 2nd index all the way to the end of the list.
print(players[-3:])#prints the last three values

print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())