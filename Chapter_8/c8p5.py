# Program for City Name, Chapter 8
def make_album(artist_name,album_title,number_song = None):
    album_details = {'a_name':artist_name,'a_title':album_title}
    if number_song:
        album_details['number_song'] = number_song

    return album_details

while True:
    print(" Please Enter the Name of the Artist,\n Name of the Album, \n Numner of song and \n enter quit when done.")
    art_name = input ("\n Please enter the name of artist.")
    if art_name == 'quit':
        break
    alb_name = input ("\n Please enter the name of album.")
    if alb_name == 'quit':
        break

    num_song = input ("\n Please enter the number of song that album contain..")
    if num_song == 'quit':
        break
    album = make_album(art_name,alb_name,num_song)
    print(album)
