import pandas as pd
from deepface import DeepFace
from paho.mqtt import client as mqtt_client
import random
import time

# Datos del broker
broker = '127.0.0.1'
port = 1883
topic = "codigoIoT/mqtt/python"
client_id = f'python-mqtt-{random.randint(0,1000)}'

# Conexion al broker
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# Subscripcion
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

#Publicador
def publish(client, mensaje):
    #while True:
    time.sleep(1)
    msg = mensaje
    result = client.publish(topic, msg)
    time.sleep(1)
    print (result)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

#buscar rostro
print ("Buscando rostro")

#df = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")
df = DeepFace.find(img_path = "/home/karen/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Imagen/face.jpg", db_path = "/home/karen/Documents/GitHub/Apertura-puertas-reconocimiento-facial/my_db", enforce_detection="false")
print("Resultado")
print(df)
print ("Imagen de mayor similitud")
print (df.identity[0]) 

client = connect_mqtt()
client.loop_start()
publish(client, df.identity[0])
