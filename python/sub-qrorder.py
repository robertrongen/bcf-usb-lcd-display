#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import datetime
import paho.mqtt.client as mqtt
import importlib
importlib.import_module('qr-sender')

orderId = 1

# Define event handlers

def on_connect(mqtt_client, obj, flags, rc):
    mqtt_client.subscribe("blokko/order")
    print("Connected")

def on_message(mqtt_client, obj, msg):
    message = msg.payload.decode()
    temp = float(message) # + 100
    print("Topic: "+msg.topic+" Payload: "+message)
    print(datetime.datetime.now())
    display_qr()
    #flp.print_str(message)
    #flp.show()

mqtt_client = mqtt.Client("", True, None, mqtt.MQTTv31)

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect("broker.hivemq.com", 1883, 60)

mqtt_client.loop_forever()
