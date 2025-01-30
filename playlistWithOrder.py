import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

#cache path for token storage
cache_path = os.path.join(os.getcwd(), '.cache')


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='', #id taken from spotify dev api
                                               client_secret='', #secret token taken from spotify dev api
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='playlist-read-private'))


playlist_id_1 = ''  #ID of source playlist
playlist_id_2 = ''  #ID of target playlist

#gets song IDs off playlist in order and adds missing ones
def get_playlist_tracks(playlist_id):
    track_ids = []
    offset = 0
    limit = 1500

    while True:
        response = sp.playlist_tracks(playlist_id, offset=offset, limit=limit)
        tracks = response['items']
        
        if not tracks:
            break
        
        track_ids.extend([item['track']['id'] for item in tracks if item['track'] is not None])
        
        if len(tracks) < limit:
            break
        
        offset += limit

    return set(track_ids)  #return a set of track IDs for easier comparison

#get songs currently in each playlist
tracks_playlist_1 = get_playlist_tracks(playlist_id_1)
tracks_playlist_2 = get_playlist_tracks(playlist_id_2)

#finds the difference in playlists
missing_in_playlist_2 = tracks_playlist_1 - tracks_playlist_2

if missing_in_playlist_2:
    print("Tracks missing in the second playlist:")
    for track_id in missing_in_playlist_2:
        track = sp.track(track_id)
        print(f"{track['name']} by {', '.join(artist['name'] for artist in track['artists'])} (ID: {track_id})")
else:
    print("No tracks are missing in the second playlist.")
