def city_country(city, country):
    return f"{city.title()}, {country.title()}"

# Calling the function 3 times
print(city_country('santiago', 'chile'))
print(city_country('tokyo', 'japan'))
print(city_country('cape town', 'south africa'))

#album
def make_album(artist, title, num_songs=None):
    album = {
        'artist': artist.title(),
        'title': title.title()
    }
    if num_songs:
        album['songs'] = num_songs
    return album

# Three albums
print(make_album('wizkid', 'made in lagos'))
print(make_album('beyonce', 'renaissance'))
print(make_album('taylor swift', 'midnights', 13))

#user albums
def make_album(artist, title, num_songs=None):
    album = {'artist': artist.title(), 'title': title.title()}
    if num_songs:
        album['songs'] = num_songs
    return album

while True:
    print("\nLet's make an album! (type 'quit' anytime to stop)")
    artist = input("Enter artist name: ")
    if artist.lower() == 'quit':
        break

    title = input("Enter album title: ")
    if title.lower() == 'quit':
        break

   
    songs = input("How many songs? (Press 'quit' to skip): ")
    if songs.lower() == 'quit':
        break

    if songs:
        album = make_album(artist, title, int(songs))
    else:
        album = make_album(artist, title)

    print("Album created:", album)

