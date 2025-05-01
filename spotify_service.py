import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyAPI:
    def __init__(self):
        self.client_id = 'your_client_id'
        self.client_secret = 'your_client_secret'
        self.auth_manager = SpotifyClientCredentials(
            client_id=self.client_id,
            client_secret=self.client_secret)
        self.sp = spotipy.Spotify(auth_manager=self.auth_manager)
    
    def search_tracks(self, query, limit=5):
        return self.sp.search(q=query, type='track', limit=limit)
    
    def get_audio_features(self, track_id):
        return self.sp.audio_features([track_id])[0]