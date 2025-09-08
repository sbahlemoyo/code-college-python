# Return Values

# returning a simple value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an arguyment optional

def get_formatted_name2(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name}  {last_name}"
    return full_name.title()

musician = get_formatted_name2('John', 'lee', 'hooker')
print(musician)

def get_formatted_name3(first_name, last_name, middle_name=''):
    """Return a neatly formatted name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{full_name} {last_name}"
    return full_name

musician = get_formatted_name3("jimi", "hendrix")
print(musician)

musician = get_formatted_name3("john", "lee", "hooker")
print(musician)

