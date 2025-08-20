#FOR LOOP

magicians = ['alice', 'david', 'carolina',]
for magician in magicians:
    # print(magicians)
    print(f'{magician.title()}, that was a great trick.')#We can do a lot with each item in our list in a for loop. We can use it inside f strings via the temporary variable in this case 'magician'
    print(f'We can\'t wait to see your next trick, {magician.title()}.\n')

#breaking out of a loop by not indenting the next line of code
print('Thank you everyone. That was a great show!')




