import requests
from bs4 import BeautifulSoup

# Replace with your Genius API access token
api_token = '6Ek7M20o4VbZJI6J9zc2fYuU7guJk73BWBrroTeV3mLuJDzM8BFrc4agVnjN09Ip'

# Specify the song title and artist
song_title = 'Imagine'
artist_name = 'John Lennon'

# Create a search query for the song
search_query = f'{song_title} {artist_name}'

# Make a request to the Genius API to search for the song
base_url = 'https://api.genius.com'
search_url = f'{base_url}/search?q={search_query}'
headers = {'Authorization': f'Bearer {api_token}'}
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
    print(lyrics)
else:
    print('Lyrics not found on the page.')
