#from typing import Text
from paho import mqtt
import speech_recognition as sr
import playsound
import os
import random
from gtts import gTTS
import webbrowser
import time
from time import ctime
from paho.mqtt import client as mqtt_client
from threading import Thread
from time import sleep
import threading
import vlc
import math
import datetime
from datetime import datetime
import pandas as pd
from speech_recognition import Microphone, Recognizer, UnknownValueError
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth

from maths import *
from pepper import *
from conversation import *
from search import *
from spotify import *
from lights import *
from timer_time import *
from temperature import *




r = sr.Recognizer()

p = vlc.MediaPlayer("sample3.mp3")

send_message = 0
start_time = 0
playing = 0


topic = 'ai/tempsensor/main'
topic3 = 'ai/tempsensor/request/main'




broker = '192.168.1.25'
port = 1883
topic = "/python/mqtt"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = ''
password = ''


# Set variables from setup.txt for spotify
setup = pd.read_csv('/home/benbobjo/code/voice assistant/setup.txt', sep='=', index_col=0, squeeze=True, header=None)
client_id = setup['client_id']
client_secret = setup['client_secret']
device_name = setup['device_name']
redirect_uri = setup['redirect_uri']
scope = setup['scope']
username = setup['username']


# Connecting to the Spotify account
auth_manager = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    username=username)
spotify = sp.Spotify(auth_manager=auth_manager)


# Selecting device to play from
devices = spotify.devices()
deviceID = None
for d in devices['devices']:
    d['name'] = d['name'].replace('’', '\'')
    if d['name'] == device_name:
        deviceID = d['id']
        break

def connect_mqtt():
    #def on_connect(client, userdata, flags, rc):
        #if rc == 0:
         #   print("Connected to MQTT Broker!")
            #
       # else:
        #    print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    #client.on_connect = on_connect
    client.connect(broker, port)
    return client









def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            jarvis_speak(ask)
            print(ask)
        r.adjust_for_ambient_noise(source)  # here
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            #jarvis_speak("i didn't catch that")
            pass
        except sr.RequestError:
            jarvis_speak('sorry, my speech service is down')
        return voice_data


def jarvis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def filtersearch(s):
    search = s
    searchitem =[s]
    notsearchwords= ['search','for','Jarvis','look','up','jarvis','jervis','Jervis'] 
    search = [" ".join([w for w in t.split() if not w in notsearchwords]) for t in searchitem]
    
    return search

def filtermaths(s):
    search = s
    searchitem =[s]
    notsearchwords= ['what','is','Jarvis',"what's"'jarvis','jervis','Jervis',"'s"] 
    search = [" ".join([w for w in t.split() if not w in notsearchwords]) for t in searchitem]
    #print(search)
    return search




def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    print(str1)
    return str1 


#def publish(client):
    #while True:
        
        #msg = 'cheese'
        #client.publish(topic, msg)
            
        

    









def respond(voice_data):
    #if 'Jarvis' in voice_data or 'Jervis' in voice_data:
        topic = 'ai/tempsensor/value/main'
        topic3 = 'ai/tempsensor/request/main'
        

        global playing

        client = connect_mqtt()
        client.loop_start()
        client.subscribe(topic)


        #spotify
        currently_playing = current_playing


        #timer_thread = Thread(target=timer)

        #timer_thread.start()
        #client.on_message = on_message


        if 'what is your name' in voice_data or "what's your name" in voice_data:
            jarvis_speak('my name is jarvis')
        
        if 'what time is it' in voice_data:
            obj_now = datetime.now()
            full_time = str(obj_now.hour) + ':' + str(obj_now.minute)
            answer = time_short(full_time)
            jarvis_speak(answer)
           


        if 'search' in voice_data:
            answer = search(voice_data)
            jarvis_speak(answer)

        if 'look up' in voice_data:
            answer = search(voice_data)
            jarvis_speak(answer)

        if 'find location' in voice_data:
            location = record_audio('What is the location')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            jarvis_speak('here is the location of ' + location)

        if 'find place' in voice_data:
            location = record_audio('What is the location')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            jarvis_speak('here is the location of ' + location)


        if 'how' in voice_data and 'you' in voice_data:
            how_they_are = record_audio("i'm good, how are you")
            print(how_they_are)
            jarvis_speak('OK')
            jarvis_speak("what do you want to do?")


        if "don't" in voice_data and 'know' in voice_data:
            what_do = record_audio("hmm, do you want to play some music?")
            if 'yeah' in what_do or 'sure' in what_do or "OK" in what_do or 'okay' in what_do:
                jarvis_speak('im singing lalalalalalalalalalalala')


        if 'stop' in voice_data:
            stop()




        if ' x ' in voice_data:
            answer = multiply(voice_data)
            jarvis_speak(answer)
        if ' / ' in voice_data:
            answer = divide(voice_data)
            jarvis_speak(answer)


        if ' + ' in voice_data:
            answer = addition(voice_data)
            jarvis_speak(answer)


        if ' - ' in voice_data:
            answer = subtraction(voice_data)
            jarvis_speak(answer)

            
        
        












        if 'lights' in voice_data or 'LED' in voice_data or 'light' in voice_data or 'LEDs' in voice_data:
            answer = lights(voice_data)












        if 'temperature' in voice_data:
            answer = temperature()
            jarvis_speak(answer)




        if 'timer' in voice_data:
            say = timer(voice_data)
            
            

        

       
            

        if 'pause' in voice_data:
            pause_spotify(spotify=spotify, device_id=deviceID)
            
            

        if 'play' in voice_data:
            words = voice_data.split()

            if 'play spotify' in voice_data or 'play Spotify' in voice_data:
                play_spotify(spotify=spotify, device_id=deviceID)
                
            elif not len(words) <= 1 and not 'play Spotify' in voice_data:
                song = voice_data
                song = filter_spotify(song)
                print(song)
                song = listToString(song)
                name = song
                uri = get_track_uri(spotify=spotify, name=name)
                print(uri)
                play_track(spotify=spotify, device_id=deviceID, uri=uri)
            else:
            #play spotify regardless
              #  play_spotify(spotify=spotify, device_id=deviceID)
                pass

        if 'exit' in voice_data:
            exit()
    




#def run():
   # client = connect_mqtt()
    #client.loop_start()
    #publish(client)
    
    


#if __name__ == '__main__':

    


#jarvis_speak('how can i help you?')
#while 1:
        #client = connect_mqtt()
        #client.loop_start()
 #       voice_data = record_audio()
  #      respond(voice_data)
   #     timer_thread = Thread(target=timer)
    #    timer_thread.start()
        #run()


def main():
  

    voice_data = record_audio()
    respond(voice_data)

#def main2():
    #print('hi')
    
    
   # print(currently_playing)
    

while 2 > 1:
    main()
    #main2()

