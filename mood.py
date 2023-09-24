import requests
from bs4 import BeautifulSoup

# Replace with your Genius API access token
api_token = '6Ek7M20o4VbZJI6J9zc2fYuU7guJk73BWBrroTeV3mLuJDzM8BFrc4agVnjN09Ip'

# Specify the desired mood (e.g., 'happy', 'sad', 'energetic', 'calm')
desired_mood = 'sad'

# Define the Genius API base URL
base_url = 'https://api.genius.com'

# Define the headers for the API request
headers = {'Authorization': f'Bearer {api_token}'}

# Function to fetch songs based on mood
def fetch_songs_by_mood(desired_mood):
    # Make a request to the Genius API to search for songs with the specified mood in lyrics
    base_url = 'https://api.genius.com'
    search_query = f'mood {desired_mood}'  # Search for songs with the specified mood
    search_url = f'{base_url}/search?q={search_query}'
    headers = {'Authorization': f'Bearer {api_token}'}
    response = requests.get(search_url, headers=headers)
    data = response.json()

    # Extract song titles and artists
    songs = []
    for hit in data['response']['hits']:
        song_title = hit['result']['title']
        artist_name = hit['result']['primary_artist']['name']
        songs.append({'title': song_title, 'artist': artist_name})
    
    return songs

# Fetch songs based on mood
songs = fetch_songs_by_mood(desired_mood)

# Initialize a list to store lyrics for the fetched songs
all_lyrics = []

# Loop through the fetched songs and parse HTML for each song's lyrics
for song in songs:
    song_title = song['title']
    artist_name = song['artist']

    # Create a search query for the song
    search_query = f'{song_title} {artist_name}'

    # Make a request to the Genius API to search for the song
    search_url = f'{base_url}/search?q={search_query}'
    response = requests.get(search_url, headers=headers)
    data = response.json()

    # Extract the URL of the song lyrics page
    song_url = data['response']['hits'][0]['result']['url']

    # Make a request to the song lyrics page to scrape the lyrics
    lyrics_response = requests.get(song_url)
    lyrics_html = lyrics_response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(lyrics_html, 'html.parser')

    # Find and extract the lyrics (lyrics are typically inside a 'div' element with class 'lyrics')
    lyrics_div = soup.find('div', class_='lyrics')
    if lyrics_div:
        lyrics = lyrics_div.get_text()
        all_lyrics.append({'title': song_title, 'artist': artist_name, 'lyrics': lyrics})
    else:
        print(f'Lyrics not found for "{song_title}" by {artist_name}.')

# Now, all_lyrics contains the lyrics for songs with the specified mood
for song_data in all_lyrics:
    print(f"Title: {song_data['title']}")
    print(f"Artist: {song_data['artist']}")
    print(f"Lyrics: {song_data['lyrics']}\n")

def fetch_songs_with_labels(desired_mood):
    # Make a request to the Genius API to search for songs with the specified mood in lyrics
    search_query = f'mood {desired_mood}'  # Search for songs with the specified mood
    search_url = f'{base_url}/search?q={search_query}'
    headers = {'Authorization': f'Bearer {api_token}'}
    response = requests.get(search_url, headers=headers)
    data = response.json()

    # Extract song titles and artists
    songs = []
    for hit in data['response']['hits']:
        song_title = hit['result']['title']
        artist_name = hit['result']['primary_artist']['name']
        lyrics = fetch_lyrics(hit['result']['url'])  # You can create a function to fetch lyrics
        songs.append({'title': song_title, 'artist': artist_name, 'lyrics': lyrics, 'mood': desired_mood})
    
    return songs

  # Function to fetch lyrics from the song's Genius page
def fetch_lyrics(song_url):
    # Make a request to the song's Genius page
    response = requests.get(song_url)
    if response.status_code != 200:
        print(f"Failed to fetch lyrics from {song_url}. Status code: {response.status_code}")
        return None
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find and extract the lyrics (lyrics are typically inside a 'div' element with class 'lyrics')
    lyrics_div = soup.find('div', class_='lyrics')
    
    if lyrics_div:
        # Extract and return the lyrics text
        lyrics = lyrics_div.get_text()
        return lyrics
    else:
        print("Lyrics not found on the page.")
        return None



# Fetch songs and assign mood labels
songs = fetch_songs_with_labels(desired_mood)

# Create a DataFrame or store the data in a CSV file with columns: 'title', 'artist', 'lyrics', 'mood'
# You can use pandas to create a DataFrame and store it as a CSV file
import pandas as pd

df = pd.DataFrame(songs)
df.to_csv('labeled_songs.csv', index=False)