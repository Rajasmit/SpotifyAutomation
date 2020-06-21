import os


from spotify_client import SpotifyClient
from youtube_client import YoutubeClient


def run():
    youtube_client = YoutubeClient('./creds/client_secret.json')
    spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
    playlists = youtube_client.get_playlists()

    for index, playlists in enumerate(playlists):
        print(f"{index}: {playlist.title}")

    choice = int(input("Enter your Choice: "))
    chosen_playlist = playlists[choice]

    print(f"You Selected: {chosen_playlist.title}")

    songs = youtube_client.get_video(chosen_playlist.id)
    print(f"Attmepting to add {len(sonfs)}")

    for song in songs:
        spotify_song_id = spotify_client.search_song(song.artist, song.track)
        if spotify_song_id:
            added_song = spotify_client.add_song_to_spotify(spotify_song_id)
            if added_song:
                print(f"Added {song.artist}")
