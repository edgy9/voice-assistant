import time
from time import ctime
from threading import Thread
from time import sleep
import threading



# define the countdown func.
#def countdown(t):
 #   t = t * 1000
  #  seconds = int(round(time.time() * 1000))
   # start_time = seconds
    #current_time = seconds
    #while start_time + t != current_time:
     #   seconds = int(round(time.time() * 1000))
      #  current_time = seconds
        #mins, secs = divmod(t, 60)
        #timer = '{:02d}:{:02d}'.format(mins, secs)
       # print(timer, end="\r")
        #print('h')
        #t -= 1

   # return('end')
  
def timer():
    print("hello, world")



# input time in seconds

  
# function call
def main():
    print('2')
    t = threading.Timer(3.0, timer)
    t.start()  # after 30 seconds, "hello, world" will be printed
    print('1')
    sleep(1)

while 2 > 1:
    main()