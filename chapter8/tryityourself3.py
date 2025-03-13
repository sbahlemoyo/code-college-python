# def city_country(city, country):
#     formatted_city_country = f'{city}, {country}'
#     return formatted_city_country.title()

# new_format = city_country('johannesburg', 'south africa')
# new_format2 = city_country('lagos', 'nigeria')
# new_format3 = city_country('nairobi', 'kenya')

# print(new_format)
# print(new_format2)
# print(new_format3)

# def make_album(artist, album_title, num_of_songs = None):
#     album = {
#         'Artist':artist.title(),
#         'Album_title': album_title.title()
         

#     }
#     if num_of_songs:
#         album['Songs'] = num_of_songs
#     return album

# album1 = make_album('beyonce', 'b-day')
# print(album1)
# album2 = make_album('kendrick lamar', 'to pimp a butterfly')
# print(album2)
# album3 = make_album('taylor swift', '22')
# print(album3)
# album2 = make_album('kendrick lamar', 'to pimp a butterfly', 10)
# print(album2)

def make_album(artist, album_title):
    album = {
        'Artist':artist.title(),
        'Album_title': album_title.title()
    }
    return album
    

while True:
        ask_exit = input('To exit enter "exit"')
        if ask_exit =='exit':
            break
        else:
         ask_album_artist = input('Enter artist')
         ask_album_title = input('Enter title of album')
         new_album = make_album(ask_album_artist, ask_album_title)
         for key, value in new_album.items():
             print(f'{key} : {value}')
        
         





