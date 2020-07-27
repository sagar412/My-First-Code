# Program for City Name, Chapter 8
def make_album(artist_name,album_title,number_song = None):
    album_details = {'a_name':artist_name,'a_title':album_title}
    if number_song:
        album_details['number_song'] = number_song

    return album_details

a = make_album('A R Rehman', 'Rang De Basanti', '7')
print(a)
b = make_album('Sonu Nigam', 'Kal ho na ho')
print(b)
c = make_album('Himesh Reshamiya',' Tera suroor','9')
print(c)
