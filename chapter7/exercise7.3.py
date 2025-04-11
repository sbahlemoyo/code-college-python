sandwich_orders = ['tuna', 'chicken', 'veggie', 'beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"✔️ {sandwich.capitalize()} sandwich")

#no pastrami
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'veggie', 'pastrami', 'chicken']
finished_sandwiches = []

print("Sorry, we're all out of pastrami today. 😔")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches we made today:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.capitalize()} sandwich")

#dream vacation
responses = {}

polling_active = True

while polling_active:
    name = input("What's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    responses[name] = place

    repeat = input("Would you like to let someone else respond? (yes/no) ")
    if repeat.lower() != 'yes':
        polling_active = False

print("\n--- Dream Vacation Results ---")
for name, place in responses.items():
    print(f"{name.title()} would love to visit {place.title()}")
