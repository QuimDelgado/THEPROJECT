#!/usr/bin/env python3
"""
rfid.py
Quim Delgado
"""

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def read():
    reader = SimpleMFRC522()
    try:
            id, text = reader.read()
            return id, text

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

    finally:
        GPIO.cleanup()


def write():    
    reader = SimpleMFRC522()
    try:
            text = input('Escriu al tag: ')
            print("Apropa el tag")
            reader.write(text)
            print("Yasta :D")

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    write()
    read()
