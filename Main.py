import spotipy
from spotipy.oauth2 import SpotifyOAuth
from google import genai
from google.genai import types 
from dotenv import load_dotenv


class AiAgentSpotifySongsRecommendation:
    def __init__(self):
        self.scope = "user-top-read"
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
        return self.reponse.text



if __name__ == "__main__":
    spotify = AiAgentSpotifySongsRecommendation()
    my_top_artist = spotify.get_df_top_artist(limit=10,offset=0,time_range="short_term")
    my_top_tracks = spotify.get_df_top_tracks(limit=10,offset=0,time_range="short_term")
    recommendations = spotify.create_list_recommendation(20,my_top_artist,my_top_tracks)
    
    print(recommendations)


