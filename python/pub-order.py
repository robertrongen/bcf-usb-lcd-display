import time
import datetime

import paho.mqtt.client as mqtt

orderId = 1

def on_connect(mqtt_client, obj, flags, rc):
    print("Connected")

# Define on_publish event Handler
def on_publish(client, userdata, mid):
    print("Message Published...")

mqtt_client = mqtt.Client("", True, None, mqtt.MQTTv31)
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish

print("Publishing orderId via MQTT to broker.hivemq.com with topic blokko/order (CTRL-C to exit)")

#mqtt_client.loop_forever()
try:
    while True:
        #timestamp = datetime.datetime.now().isoformat()
        mqtt_client.connect("broker.hivemq.com",1883)
        mqtt_client.publish("blokko/order",orderId)
        #print(orderId,"| ",timestamp)
        mqtt_client.disconnect()
        time.sleep(10)

# exit the script with ctrl-c
except KeyboardInterrupt:
    print("Session interrupted")


