from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace these with your actual Spotify API credentials
CLIENT_ID = "your_client_id"
SECRET_KEY = "your_secret_key"
REDIRECT_URI = "http://example.com"  # Use your desired redirect URI

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=SECRET_KEY,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    if result["tracks"]["items"]:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    else:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(f"Playlist created: {playlist['name']}")
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"{len(song_uris)} songs added to the playlist.")




# from bs4 import BeautifulSoup
# import requests
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth



# # Scraping Billboard 100
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
# soup = BeautifulSoup(response.text, 'html.parser')
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]

# #Spotify Authentication
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id=CLIENT_ID,
#         client_secret=SECRET_KEY,
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )
# user_id = sp.current_user()["id"]
# print(user_id)

# #Searching Spotify for songs by title
# song_uris = []
# year = date.split("-")[0]
# for song in song_names:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")

# #Creating a new private playlist in Spotify
# playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

# #Adding songs found into the new playlist
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)



"""
#============================================================

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=SECRET_KEY,
        show_dialog=True,
        cache_path="token.txt",
        username="Uri Gakuru",
    )
)
user_id = sp.current_user()["id"]
print(user_id)


#searching spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify. Skipped")



song_uris = ["The lis of", "song URIs", "you got by", "searching spotify"]


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)


sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


#=============================================
"""









# import requests
# from bs4 import BeautifulSoup


# date = input("Which year would you like to travel to? Type the date in this format YYYY-MM-DD: ")
# url = "https://www.billboard.com/charts/hot-100/" + date

# respose = requests.get(url)

# soup = BeautifulSoup(respose.text, "html.parser")
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]




# #  id="title-of-a-story",

# # response = requests.get(url)
# # data = response.text

# # soup = BeautifulSoup(data, "html.parser")
# # section_heading = soup.find_all(name="h3", id="title-of-a-story", class_="c-title")
# # song_names = [song.getText().strip() for song in section_heading]

# # print(song_names)

# with open("songs.txt", mode="w") as file:
#     for song in song_names:
#         file.write(f"{song}\n")






# from bs4 import BeautifulSoup
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# import os


# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: \n")
# url = f"https://www.billboard.com/charts/hot-100/{date}/"
# response = requests.get(url)
# web_page = response.text
# soup = BeautifulSoup(web_page, "html.parser")
# song_soup = soup.find_all("h3", "a-no-trucate")
# song_names = [s.getText(strip=True) for s in song_soup]
# spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("client_id"),
#                                                     client_secret=os.environ.get("client_secret"),
#                                                     redirect_uri="http://example.com",
#                                                     scope="playlist-modify-private"))

# user = spotify.current_user()['id']
# name = f"{date} Billboard 100"
# print(f"Generating a playlist for user: {user} called {name}")

# playlist_id = spotify.user_playlist_create(user, name, public=False, collaborative=False,
#                                            description=f'The top 100 songs on {date}')['id']


# def get_track_id(song):
#     track_id = spotify.search(song, limit=1)['tracks']['items'][0]['uri']
#     return track_id


# track_ids = [get_track_id(song) for song in song_names]
# spotify.playlist_add_items(playlist_id, track_ids)
# print("Complete")


# # from bs4 import BeautifulSoup
# # import requests
# # import spotipy
# # from spotipy.oauth2 import SpotifyOAuth



# # # Scraping Billboard 100
# # date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# # response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
# # soup = BeautifulSoup(response.text, 'html.parser')
# # song_names_spans = soup.select("li ul li h3")
# # song_names = [song.getText().strip() for song in song_names_spans]

# # #Spotify Authentication
# # sp = spotipy.Spotify(
# #     auth_manager=SpotifyOAuth(
# #         scope="playlist-modify-private",
# #         redirect_uri="http://example.com",
# #         client_id=CLIENT_ID,
# #         client_secret=SECRET_KEY,
# #         show_dialog=True,
# #         cache_path="token.txt",
# #         username="Uri Gakuru",
# #     )
# # )
# # user_id = sp.current_user()["id"]
# # print(user_id)

# # #Searching Spotify for songs by title
# # song_uris = []
# # year = date.split("-")[0]
# # for song in song_names:
# #     result = sp.search(q=f"track:{song} year:{year}", type="track")
# #     print(result)
# #     try:
# #         uri = result["tracks"]["items"][0]["uri"]
# #         song_uris.append(uri)
# #     except IndexError:
# #         print(f"{song} doesn't exist in Spotify. Skipped.")

# # #Creating a new private playlist in Spotify
# # playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# # print(playlist)

# # #Adding songs found into the new playlist
# # sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

# # # # import spotipy
# # # # from spotipy.oauth2 import SpotifyOAuth
# # #

# # #
# # # # Initialize Spotipy with the SpotifyOAuth manager
# # # sp = spotipy.Spotify(
# # #     auth_manager=SpotifyOAuth(
# # #         scope="playlist-modify-private",
# # #         redirect_uri=REDIRECT_URI,
# # #         client_id=CLIENT_ID,
# # #         client_secret=SECRET_KEY,
# # #         show_dialog=True,
# # #         cache_path="token.txt",
# # #         username="Uri Gakuru",  # Replace with your Spotify username
# # #     )
# # # )
# # #
# # # # Get the current user's ID
# # # user_id = sp.current_user()["id"]
# # # print(f"Your Spotify user ID: {user_id}")
# # #
# # #
# # #
# # #
# # # # import spotipy
# # # # from spotipy.oauth2 import SpotifyOAuth
# # # #

# # # #
# # # # sp = spotipy.Spotify(
# # # #     auth_manager=SpotifyOAuth(
# # # #         scope="playlist-modify-private",
# # # #         redirect_uri=REDIRECT_URI,
# # # #         client_id=CLIENT_ID,
# # # #         client_secret=SECRET_KEY,
# # # #         show_dialog=True,
# # # #         cache_path="token.txt",
# # # #         username="Uri Gakuru",
# # # #     )
# # # # )
# # # # user_id = sp.current_user()["id"]
# # # # print(user_id)
# # #
# # # # scope = "user-library-read"
# # # # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
# # #
# # # # results = sp.current_user_saved_tracks()






# # # # for idx, item in enumerate(results['items']):
# # # #     track = item['track']
# # # #     print(idx, track['artists'][0]['name'], " – ", track['name'])
# # #
# # #
# # # # import spotipy
# # # # from spotipy.oauth2 import SpotifyOAuth
# # #
# # # # sp = spotipy.Spotify(
# # # #     auth_manager=SpotifyOAuth(
# # # #         scope="playlist-modify-private",
# # # #         redirect_uri="http://example.com",
# # # #         client_id=CLIENT_ID,
# # # #         client_secret=SECRET_KEY,
# # # #         show_dialog=True,
# # # #         cache_path="token.txt",
# # # #         username=vuhaa7dtto3z08p9p2uk6op1s,
# # # #     )
# # # # )
# # # # user_id = sp.current_user()["id"]
