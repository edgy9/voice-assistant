from paho.mqtt import client as mqtt_client
import random
import time
from time import ctime


broker = '192.168.1.25'
port = 1883

topic2 = "ai/tempsensor/main"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = ''
password = ''

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    topic = "ai/tempsensor/main"
    def on_message(client, userdata, msg):        
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message



def publish(client):
    
    while True:
        time.sleep(1)
        i = 0
        while i < 1:
            msg = ctime()
            #result = client.publish(topic, str(msg))
            #print('sent messagew' + str(msg))
           # status = result[0]
           # if status == 0:
                #print(f"Send `{msg}` to topic `{topic}`")
           # else:
            #    print(f"Failed to send message to topic {topic}")
          #  i += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    subscribe(client)
    publish(client)
    


#if __name__ == '__main__':
if 2 > 1:
    run()