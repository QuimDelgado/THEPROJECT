#!/usr/bin/env python3
"""
rfid.py
Quim Delgado
"""

import RPi.GPIO as GPIO
from send import sendToServerID
from i2c import instancia_display as display
from mfrc522 import SimpleMFRC522
import time

def read():
    reader = SimpleMFRC522()
    try:
        id, text = reader.read()
        return id, text
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
    finally:
        GPIO.cleanup()

def readRfid():
    display.draw_text("Apropa el Tag al lector -------->")
    id, text = read()
    print(f"ID: {id}\nText: {text}")
    display.draw_text("Identificant el Tag")
    respostaServerID = sendToServerID(text)
    if respostaServerID != "false":
        display.draw_text(f"Mira a la camara")
        time.sleep(3)
    return respostaServerID

if __name__ == "__main__":
    readRfid()
