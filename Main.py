import spotipy
from spotipy.oauth2 import SpotifyOAuth
from google import genai
from google.genai import types 
from dotenv import load_dotenv
from datetime import datetime
import json


class AiAgentSpotifySongsRecommendation:
    def __init__(self):
        self.scope = "user-top-read playlist-modify-public playlist-modify-private"
        load_dotenv()
        self.client = genai.Client()
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope))
        self.list_my_top_artist = []
        self.list_my_top_tracks = []


    def get_df_top_artist(self,limit,offset,time_range):
        top_artist = self.sp.current_user_top_artists(limit=limit, offset=offset, time_range=time_range)
        for artist in top_artist['items']:
            self.list_my_top_artist.append(f"Name artist: {artist['name']} and his genders are {','.join(artist['genres'])}")
        return self.list_my_top_artist


    def get_df_top_tracks(self,limit,offset,time_range):

        top_tracks = self.sp.current_user_top_tracks(limit=limit,offset=offset,time_range=time_range)
        for track in top_tracks['items']:
            self.list_my_top_tracks.append(f"Name track: {track['name']} and his main singer is {track['artists'][0]['name']}")
        return self.list_my_top_tracks

    def create_list_recommendation(self,size_list,my_top_artist,my_top_tracks):
             
        self.reponse = self.client.models.generate_content(
            model = "gemini-2.5-flash",
            contents=f"Give me {size_list} music recommendations based on information from my top artists ({'-'.join(my_top_artist)}) and my top tracks on Spotify ({'-'.join(my_top_tracks)})",
            config=types.GenerateContentConfig(
                system_instruction="You are a specialist recommendation of tracks and artist and based on my task of tracks and artists you give to me a list of tracks based on my task of music. You will only give to me option that exist on spotify. Give as output only in the format of a variable of list of string to be use on a python code [], don't send any other message with"
                
            )          
        )
        return json.loads(self.reponse.text)

    def create_new_playlist(self):
     current_month = datetime.now().strftime("%B")
     playlist_created_id = self.sp.user_playlist_create(user="repplayy01",name=f"MKAgent: {current_month} recommedation", description="Playlist recommended by MkAgent")
     return playlist_created_id["id"]
     
 
 
    def get_tracks_ids(self,track):
        search_result = self.sp.search(q=track, limit=1, offset=0, market="BR")
        id_track = search_result['tracks']['items'][0]['id']
        return id_track
    
    def add_tracks_to_playlist(self,playlist_id,tracks):
     self.sp.playlist_add_items(playlist_id=playlist_id,items=tracks)



if __name__ == "__main__":
    spotify = AiAgentSpotifySongsRecommendation()
    list_format_add_tracks = []
    my_top_artist = spotify.get_df_top_artist(limit=10,offset=0,time_range="short_term")
    my_top_tracks = spotify.get_df_top_tracks(limit=10,offset=0,time_range="short_term")
    recommendations = spotify.create_list_recommendation(5,my_top_artist,my_top_tracks)
    
              
    spotify.add_tracks_to_playlist(playlist_id= spotify.create_new_playlist(),tracks=recommendations)
        
    
    print("success in create new playlist recommedation")


