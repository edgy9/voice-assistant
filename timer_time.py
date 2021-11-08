import threading
import time
from datetime import datetime
import vlc
import math



p = vlc.MediaPlayer("sample3.mp3")

def timer1():
    print("hello, world")
    p.play()

def stop():
    p.stop()

def how_long_timer():
    start_time = time.time()
    return(start_time)



def filtertimer(s):
    search = s
    searchitem =[s]
    notsearchwords= ['set','Set','timer','a','Timer','for','For','start','Start','Jervis','jarvis','Jarvis','jervis'] 
    search = [" ".join([w for w in t.split() if not w in notsearchwords]) for t in searchitem]
    #print(search)
    return search

def filtertimer2(s):
    search = s
    searchitem =[s]
    notsearchwords= ['hour','hours','Hour','Hours','minutes','Minutes','Minute','minute','second','Second','seconds','Seconds','min','mins'] 
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
        
def hour(s):
    s = int(s) * 60
    s = int(s) * 60
    return(s)

def minute(s):
    print(s)
    s = int(s) * 60
    return(s)

def how_long_timer():
    start_time = time.time()
    return(start_time)

def how_long_timer_left(start_time):
    start_time = start_time
    runing_time = (time.time()-start_time)
    time_left = timer_legnth - runing_time
    time_left1 = str(time_left)
    print (str(time_left) + "seconds left")
    time_left = math.floor(time_left)
    full_time_left = str(datetime.timedelta(seconds=time_left))
    print(full_time_left)
    # how_long_timer()
    return(full_time_left)

def timer(voice_data):
    global start_time 
    global timer_legnth
    if 'set' in voice_data or 'start' in voice_data:
        
        s = voice_data
        
        s = filtertimer(s)
        s = listToString(s)
        #print(s)
        if 'hour' in s or 'hours' in s:
            s = filtertimer2(s)
            s = listToString(s)
           # print(s + '2')
            if 'an' in s or '1-hour' in s:
                s = '1'
                #print('2')
            if '2-hours' in s or '2-hour' in s:
                s = '2'
            if '3-hours' in s or '3-hour' in s:
                s = '3'
            if '4-hours' in s or '4-hour' in s:
                s = '4'
            if '5-hours' in s or '5-hour' in s:
                s = '5'
            if '6-hours' in s or '6-hour' in s:
                s = '6'
          #  print(s)
            s = hour(s)
           # print(s)
        else:
            if 'minutes' in s or 'minute' in s or 'min' in s:
                s = filtertimer2(s)
                s = listToString(s)
            # print(s)
                if 'a' in s or '1-minute' in s:
                    s = '1'
                    #print('2')
                if '2-minutes' in s or '2-minute' in s:
                    s = '2'
                if '3-minutes' in s or '3-minute' in s:
                    s = '3'
                if '4-minutes' in s or '4-minute' in s:
                    s = '4'
                if '5-minutes' in s or '5-minute' in s:
                    s = '5'
                if '6-minutes' in s or '6-minute' in s:
                    s = '6'
                #print()
                s = minute(s)
                #print(s)
            else:
                if 'second' in s or 'seconds' in s:
                    s = filtertimer2(s)
                    s = listToString(s)
                    #print(s)
                    if 'a' in s or '1-second' in s:
                        s = '1'
                        #print('2')
                    if '2-seconds' in s or '2-second' in s:
                        s = '2'
                    if '3-seconds' in s or '3-second' in s:
                        s = '3'
                    if '4-seconds' in s or '4-second' in s:
                        s = '4'
                    if '5-seconds' in s or '5-second' in s:
                        s = '5'
                    if '6-seconds' in s or '6-second' in s:
                        s = '6'
                    
        print(s)


        t = threading.Timer(int(s), timer1)
        timer_legnth = s
        start_time = time.time()
        t.start()  
    
    if 'what' in voice_data or 'how' in voice_data:
        how_long = how_long_timer_left(start_time)
        return(how_long)
    else:
        pass
        

pass
def time_short(full_time):
    print(full_time)
    hours = full_time[0:2]
    minutes = full_time[3:5]
    if ':' in hours:
        hours = full_time[0:1]
        minutes = full_time[2:4]
    
    #print(hours)
    #print(minutes)

    time_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
    hour_list = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']
    short_min_list = ['five past,ten past','quarter past','twenty past', 'twenty five past', 'half', 'twenty five to', 'twenty to', 'quarter to', 'ten to', 'five to',' ']
    index_hours = time_list.index(hours)
    #print(index_hours)


    if index_hours > 12:
        index_hours = index_hours - 12
     
    
   
    
    minutes1 = int(minutes)
    if minutes1 > 32 and minutes1 < 58:
        index_hours += 1

    hour = (hour_list[index_hours])
    
    #print(minutes)
    short_time = ''
    if minutes1 >= 0 and minutes1 < 4:
        minutes = " o'clock"

        short_time = hour + minutes
    elif minutes1 > 3 and minutes1 < 8:     #five past
        minutes = 'five past '
        short_time = minutes + hour
    elif minutes1 > 7 and minutes1 < 13:    #ten past
        minutes = 'ten past '
        short_time = minutes + hour
    elif minutes1 > 12 and minutes1 < 18:   #quarter past
        minutes = 'quarter past '
        short_time = minutes + hour    
    elif minutes1 > 17 and minutes1 < 23:   #twenty past
        minutes = 'twenty past '
        short_time = minutes + hour
    elif minutes1 > 22 and minutes1 < 28:   #twenty five past
        minutes = 'twenty five past '
        short_time = minutes + hour
    elif minutes1 > 27 and minutes1 < 33:   #half
        minutes = 'half '
        short_time = minutes + hour
    elif minutes1 > 32 and minutes1 < 38:   #twenty five to
        minutes = 'twenty five to '
        short_time = minutes + hour
    elif minutes1 > 37 and minutes1 < 43:   #twenty to
        minutes = 'twenty to '
        short_time = minutes + hour
    elif minutes1 > 42 and minutes1 < 48:   #quarter to
        minutes = 'quarter to '
        short_time = minutes + hour
    elif minutes1 > 47 and minutes1 < 53:   #ten to
        minutes = 'ten to '
        short_time = minutes + hour
    elif minutes1 > 52 and minutes1 < 58:   #five to
        minutes = 'five to '
        short_time = minutes + hour        
    elif minutes1 > 57 and minutes1 < 60:   #o clock
        minutes = " o'clock"
        short_time = hour + minutes

    return(short_time)
