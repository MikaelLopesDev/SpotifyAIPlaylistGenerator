import requests
from dotenv import load_dotenv
import os



class SpotifyApiCalls:
    def __init__(self, client_id=None, client_secret=None):
        load_dotenv()
        self.client_id = client_id or os.getenv("CLIENT_ID_SPOTIFY")
        self.client_secret = client_secret or os.getenv("CLIENT_SECRET_SPOTIFY")
        self.access_token = self.authenticate()  # Chama na inicialização



    def authenticate(self):
        url = "https://accounts.spotify.com/api/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()
            return response.json()["access_token"]
        except Exception as e:
            print(f"Other error occurred: {e}")
            return None



    def get_playlist(self, artist_id):
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(
            f"https://api.spotify.com/v1/artists/{artist_id}",
            headers=headers
        )
        return response.json()
