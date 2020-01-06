#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import sub-qrorder
from __future__ import print_function
import binascii
import base64
import time
import threading

#pip install qrcode[pil]
#pip install git+git://github.com/ojii/pymaging.git#egg=pymaging 
#pip install git+git://github.com/ojii/pymaging-png.git#egg=pymaging-png
#https://pypi.org/project/qrcode/
import qrcode
from PIL import Image, ImageFont, ImageDraw
#https://pymaging.readthedocs.io/en/latest/
from qrcode.image.pure import PymagingImage

#pip install pyserial
import serial

import psutil

orientation = 0

def serial_open(port):
    return serial.Serial(
        port=port,
        baudrate=921600,
        timeout=0
    )

    #ser.isOpen()

def display_image(img, ser):
    img = img.convert('1') # convert image to black and white

    pixels = img.load()
    #pixels = img

    byte_array = [0]*(16*128)
    index = 0

    for y in range(0, 128):
        for x in range(0, 128, 8):
            for bit in range(0, 8):
                byte_array[index] |= (0 if pixels[(x + bit, y)] == 0 else 1) << (7 - bit)
            index += 1

    b64 = base64.b64encode(bytearray(byte_array))

    ser.write(b64)
    ser.write(b'\r\n')
    ser.flush()

def qrImage(_orderId):
    qr = qrcode.QRCode(
        version=5,  #The version parameter is an integer from 1 to 40 that controls the size of the QR Code
                    #the smallest, version 1, is a 21x21 matrix
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=4,
        border=4,
    )
    url = 'https://blokko.blockchainadvies.nu/receive-order.html?order=' + str(_orderId)
    qr.add_data(url)
    qrImage = qrcode.make(url, image_factory=PymagingImage)
    print(qrImage)
    return qrImage

def screen_draw():
    # Print QR code with Order ID
    img = Image.open("../img/qr-code-logo-1.png")
    img = img.resize((128, 128))
    #img = Image.new("RGB", (128, 128), (255,255,255))
    #img = qrImage(orderId)
    return (img, 0.1)

def serial_command(cmd):
    print(cmd)

def display_qr()
    print("Opening port")
    ser = False

    while True:
        try:
            ser = serial_open("/dev/ttyUSB0")
            #ser = serial_open("/COM5")

        except Exception as e:
            print("Cannot open port: " + str(e))
            time.sleep(10)

        print("Port opened")

        while (serial):
            img, delay = screen_draw()

            try:
                display_image(img, ser)

            except Exception as e:
                print(str(e))
                ser = False
                break

            time.sleep(delay)
