import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import pandas as pd

class Spotify:
    def __init__(self):
        self.scope = "user-top-read"
        # Inicialize o objeto SpotifyOAuth com o scope correto
        load_dotenv()
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope))
        self.df_my_top_artist = pd.DataFrame(columns=['Name', 'Genders'])
        self.df_my_top_tracks = pd.DataFrame(columns=['Name_song', 'Name_artist'])


    def get_df_top_artist(self,limit,offset,time_range ):
        top_artist = self.sp.current_user_top_artists(limit=limit, offset=offset, time_range=time_range)
        for artist in top_artist['items']:
            new_row = pd.DataFrame([{'Name': artist['name'], 'Genders': ','.join(artist['genres'])}])
            self.df_my_top_artist = pd.concat([self.df_my_top_artist,new_row], ignore_index=True)
        return self.df_my_top_artist


    def get_df_top_tracks(self,limit,offset,time_range):
        try:
            top_tracks = self.sp.current_user_top_tracks(limit=limit,offset=offset,time_range=time_range)
            for track in top_tracks['items']:
                new_row = pd.DataFrame([{'Name': track['name'], 'Name_artist': track['artists'][0]['name']}])
                self.df_my_top_tracks = pd.concat([self.df_my_top_tracks, new_row], ignore_index=True)
            return self.df_my_top_tracks
        except Exception as e:
            print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    spotify = Spotify()
    my_top_artirst = spotify.get_df_top_artist(limit=10,offset=0,time_range="short_term")
    my_top_tracks = spotify.get_df_top_tracks(limit=10,offset=0,time_range="short_term")
    print("ok")


