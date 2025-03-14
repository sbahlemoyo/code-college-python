# def sandwich_maker(*fillings):
#     print('Preparing sandwich with the following fillings:\n ')
#     for filling in fillings:
#         print(filling.title())
#     print('\nYour order will be ready in 15 minutes!')

# sandwich_maker('cheese', 'beef burger', 'lettuce', 'mayo')
# sandwich_maker('avocado', 'egg', 'bacon', 'tomato', 'mayo')
# sandwich_maker('shredded chicken', 'mayo', 'coleslaw', 'lettuce')

# def user_profile(first, last, **user_info):
#     ''' Build a user profile containing info about the user'''
#     user_info['First Name'] = first
#     user_info['Last_name'] = last
#     return user_info

# build_profile = user_profile('sbahle', 
#                              'asanda',
#                              age= str(22), 
#                              language= 'python', 
#                              school= 'code college')
# print(build_profile)
# for detail, info in build_profile.items():
#         print(f'{detail.title()} : {info.title()}')


def car(manufacturer, model_name, **more_info):
    more_info['Manufacturer'] = manufacturer.title()
    more_info['Model Name'] = model_name.title()
    return more_info

build_car = car('Toyota', 'Hilux', color = 'Darkgray', cost = '750 000')
print(build_car)