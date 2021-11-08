from spotipy import Spotify


class InvalidSearchError(Exception):
    pass


def get_album_uri(spotify: Spotify, name: str) -> str:
    """
    :param spotify: Spotify object to make the search from
    :param name: album name
    :return: Spotify uri of the desired album
    """

    # Replace all spaces in name with '+'
    original = name
    name = name.replace(' ', '+')

    results = spotify.search(q=name, limit=1, type='album')
    if not results['albums']['items']:
        raise InvalidSearchError(f'No album named "{original}"')
    album_uri = results['albums']['items'][0]['uri']
    return album_uri


def get_artist_uri(spotify: Spotify, name: str) -> str:
    """
    :param spotify: Spotify object to make the search from
    :param name: album name
    :return: Spotify uri of the desired artist
    """

    # Replace all spaces in name with '+'
    original = name
    name = name.replace(' ', '+')

    results = spotify.search(q=name, limit=1, type='artist')
    if not results['artists']['items']:
        raise InvalidSearchError(f'No artist named "{original}"')
    artist_uri = results['artists']['items'][0]['uri']
    print(results['artists']['items'][0]['name'])
    return artist_uri


def get_track_uri(spotify: Spotify, name: str) -> str:
    """
    :param spotify: Spotify object to make the search from
    :param name: track name
    :return: Spotify uri of the desired track
    """

    # Replace all spaces in name with '+'
    original = name
    name = name.replace(' ', '+')

    results = spotify.search(q=name, limit=1, type='track')
    if not results['tracks']['items']:
        raise InvalidSearchError(f'No track named "{original}"')
    track_uri = results['tracks']['items'][0]['uri']
    return track_uri


def play_track(spotify=None, device_id=None, uri=None):
    spotify.start_playback(device_id=device_id, uris=[uri])
    

def play_spotify(spotify=None, device_id=None):
    spotify.start_playback(device_id=device_id)


def pause_spotify(spotify=None, device_id=None, uri=None):
    spotify.pause_playback(device_id=device_id)

def current_playing(spotify=None, device_id=None):
    spotify.currently_playing(spotify=spotify,device_id=device_id)

def filter_spotify(song):
    search = song
    searchitem =[song]
    notsearchwords= ['play','Spotify','spotify','please'] 
    search = [" ".join([w for w in t.split() if not w in notsearchwords]) for t in searchitem]
    #print(search)
    return search
