def make_sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('ham', 'cheese')
make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich('peanut butter', 'jelly', 'banana', 'honey')

#userprofile
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

profile = build_profile('sbahle', 'pythonista', location='Cape Town', field='Software Engineering', mood='Vibing')
print(profile)

#cars
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
