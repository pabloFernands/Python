from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

#data_musica = input("Which year do you want to travel? Enter year, month and day in this format YYYY-MM-DD.")
data_musica = "0123456789"

if len(data_musica) == 10:
    response = requests.get(f"https://www.billboard.com/charts/hot-100/2000-08-12/")
    website_text = response.text
else:
    data_musica = input("Incorrect date.\nWhich year do you want to travel? "
                        "Enter year, month and day in this format YYYY-MM-DD.")



soup = BeautifulSoup(website_text, "html.parser")

articles_first = soup.find_all("h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s "
                                                                   "u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 "
        "u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only"
        " u-letter-spacing-0028@tablet")
music_first = [name.getText(strip=True) for name in articles_first]
#print(top_musics)

articles = soup.find_all("h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
music_top = [name.getText(strip=True) for name in articles]
#print(music_top)

music_top.append(music_first[0])

#---------------Spotify---------------

spot_id = "2b9280623c1c4d119ef9fe51d5bb947e"
spot_key = "d06018201c8b4a24910b9de7563366c5"



spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spot_id,
                                               client_secret=spot_key,
                                               redirect_uri="http://example.com",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               scope="playlist-modify-private"))

#results = spotify.current_user_saved_tracks()
results_id = spotify.current_user()["id"]
print(results_id)


song_info = []
year = data_musica.split("-")[0]
for song in music_top:
    result = spotify.search(q=f"track:{song} year:{year}", type="track", limit=1 )
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_info.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = spotify.user_playlist_create(user=results_id, name=f"{data_musica} Billboard 100", public=False)
print(playlist)
