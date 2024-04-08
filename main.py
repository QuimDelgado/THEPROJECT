#!/usr/bin/env python3
"""
main.py
Quim Delgado
"""
from time import sleep
from rfid import readRfid
from camera import take_pic
from i2c import instancia_display as display

def main():
    notRecUser = True
    print("LLIBRERIES CARREGADES")
    while notRecUser:
        print("Apropa el tag al lector")
        respostaServerID = readRfid()
        print(respostaServerID)
        if respostaServerID != "false":
            respostaServerPIC = take_pic()
            print(respostaServerPIC)
            if respostaServerPIC != "False":
                if respostaServerID == respostaServerPIC:
                    display.draw_text(f"Benvingut {respostaServerPIC} has sigut validat")
                    sleep(2)
                else:
                    display.draw_text("Usuari no coincident, torna't a validar")
                    sleep(2)
            else:
                display.draw_text("Usuari no reconegut, torna't a validar")
                sleep(2)
        else:
            display.draw_text("Usuari no reconegut, torna't a validar")
            sleep(2)


try:
    main()
except Exception as e:
    print(f"Error: {e}")
finally:
    display.clear_display()
