import vlc
import time

p = vlc.MediaPlayer("sample3.mp3")

p.play()
time.sleep(3)
p.stop()        