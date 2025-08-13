import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import pandas as pd

class AiAgentSpotifySongsRecommendation:
    def __init__(self):
        self.scope = "user-top-read"

        load_dotenv()
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope))
        self.list_my_top_artist = []
        self.list_my_top_tracks = []


    def get_df_top_artist(self,limit,offset,time_range ):
        top_artist = self.sp.current_user_top_artists(limit=limit, offset=offset, time_range=time_range)
        for artist in top_artist['items']:
            self.list_my_top_artist.append(f"Name artist: {artist['name']} and his genders are {','.join(artist['genres'])}")
        return self.list_my_top_artist


    def get_df_top_tracks(self,limit,offset,time_range):

        top_tracks = self.sp.current_user_top_tracks(limit=limit,offset=offset,time_range=time_range)
        for track in top_tracks['items']:
            self.list_my_top_tracks.append(f"Name track: {track['name']} and his main singer is {track['artists'][0]['name']}")
        return self.list_my_top_tracks




if __name__ == "__main__":
    spotify = AiAgentSpotifySongsRecommendation()
    my_top_artist = spotify.get_df_top_artist(limit=10,offset=0,time_range="short_term")
    my_top_tracks = spotify.get_df_top_tracks(limit=10,offset=0,time_range="short_term")
    print("ok")


