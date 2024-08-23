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





# import requests
# import spotipy
# from bs4 import BeautifulSoup
# from spotipy.oauth2 import SpotifyOAuth


# date = input("Which year would you like to travel to? Type the date in this format YYYY-MM-DD: ")
# url = "https://www.billboard.com/charts/hot-100/" + date
# user_id = sp.current_user()["id"]

# # Initialize Spotipy with the SpotifyOAuth manager
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri=REDIRECT_URI,
#         client_id=CLIENT_ID,
#         client_secret=SECRET_KEY,
#         show_dialog=True,
#         cache_path="token.txt",
#         username="Uri Gakuru",  # Replace with your Spotify username
#     )
# )

# # Get the current user's ID
# # user_id = sp.current_user()["id"]
# print(f"Your Spotify user ID: {user_id}")


# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]


# with open("songs.txt", mode="w") as file:
#     for song in song_names:
#         file.write(f"{song}\n")



















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