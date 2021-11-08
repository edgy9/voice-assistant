import random
from paho.mqtt import client as mqtt_client

broker = '192.168.1.25'
port = 1883
topic = "/python/mqtt"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = ''
password = ''

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

def lights(voice_data):
    topic = 'ai/tempsensor/value/main'
    topic3 = 'ai/tempsensor/request/main'

    client = connect_mqtt()
    client.loop_start()
    client.subscribe(topic)

    
    if 'all' in voice_data:
        if 'on' in voice_data:
            msg = 'on'
            topic1 = 'ai/lights/all'
            result = client.publish(topic1, str(msg))
            print('sent messagew' + str(msg))
            status = result[0]
            if status == 0:
                print(f"Send `{msg}` to topic `{topic1}`")
            else:
                print(f"Failed to send message to topic {topic1}")

        if 'off' in voice_data:
            msg = 'off'
            topic1 = 'ai/lights/all'
            result = client.publish(topic1, str(msg))
            print('sent messagew' + str(msg))
            status = result[0]
            if status == 0:
                print(f"Send `{msg}` to topic `{topic1}`")
            else:
                print(f"Failed to send message to topic {topic1}")
            
        if 'red' in voice_data or 'Red' in voice_data:
            msg = 'red'
            topic1 = 'ai/lights/all'
            result = client.publish(topic1, str(msg))
            print('sent messagew' + str(msg))
            status = result[0]
            if status == 0:
                print(f"Send `{msg}` to topic `{topic1}`")
            else:
                print(f"Failed to send message to topic {topic1}")

        if 'blue' in voice_data or 'Blue' in voice_data:
            msg = 'blue'
            topic1 = 'ai/lights/all'
            result = client.publish(topic1, str(msg))
            print('sent messagew' + str(msg))
            status = result[0]
            if status == 0:
                print(f"Send `{msg}` to topic `{topic1}`")
            else:
                print(f"Failed to send message to topic {topic1}")



        if 'green' in voice_data or 'Green' in voice_data:
            msg = 'green'
            topic1 = 'ai/lights/all'
            result = client.publish(topic1, str(msg))
            print('sent messagew' + str(msg))
            status = result[0]
            if status == 0:
                print(f"Send `{msg}` to topic `{topic1}`")
            else:
                print(f"Failed to send message to topic {topic1}")