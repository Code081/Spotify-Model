import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace with your own credentials
client_id = '4100063779124efbba13b0a17ae65950'
client_secret = '6e9a73141d4d499f9c5bdddabfe96344'

# Initialize the Spotify client with your credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Search for songs based on a query (e.g., "rock")
query = 'rock'
results = sp.search(q=query, type='track', limit=10)  # Limit to 10 results

# Extract and print song data
for track in results['tracks']['items']:
    print('Track:', track['name'])
    print('Artists:', ', '.join([artist['name'] for artist in track['artists']]))
    print('Album:', track['album']['name'])
    print('Popularity:', track['popularity'])
    print('-----------------------')
