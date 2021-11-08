import random
from paho.mqtt import client as mqtt_client



broker = '192.168.1.25'
port = 1883
topic = "/python/mqtt"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = ''
password = ''

topic = 'ai/tempsensor/value/main'
topic3 = 'ai/tempsensor/request/main'

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



def temperature():

    client = connect_mqtt()
    client.loop_start()
    client.subscribe(topic)
    
        #topic = 'ai/tempsensor/value/main'
        #topic3 = 'ai/tempsensor/request/main'
    msg1 = '123'
    client.publish(topic3, str(msg1))
    
    def on_message(client, userdata, msg):        
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        va = msg.payload.decode()
        if '.0' in va:
                va = va[:-2]
        va = va + '°C'    
        print(va)
        return(va)
    client.on_message = on_message


