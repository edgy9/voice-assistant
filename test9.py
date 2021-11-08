from spotify_local import SpotifyLocal
with SpotifyLocal() as s:
        pass

with SpotifyLocal() as s:
        s.pause()

with SpotifyLocal() as s:
        print(s.get_current_status())