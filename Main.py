from SpotifyApiCalls import SpotifyApiCalls


if __name__ == "__main__":
    spotify_client = SpotifyApiCalls()
    info_artist = spotify_client.get_playlist("1Cs0zKBU1kc0i8ypK3B9ai")
    name = info_artist["name"]
    popularity = info_artist["popularity"]
    print(f"Nome artista {name} e popularida {popularity}")

