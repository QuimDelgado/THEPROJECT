#!/usr/bin/env python3
"""
send.py
Quim Delgado
"""
import subprocess

def sendToServerID(text):
    text = text.split()[0]  # Asumiendo que deseas el primer elemento del texto dividido
    # Ejecutamos el comando curl y capturamos la salida
    try:
        response = subprocess.run(['curl', '-X', 'POST', 'https://beta-bbdd.duckdns.org/procesar_datos', '-d', f'numero_rfid={text}'], capture_output=True, text=True)
        if response.returncode == 0:
            # Procesar la respuesta
            text_response = response.stdout.strip()
            # Eliminar todos los espacios de la respuesta si es necesario
            text_response = text_response.replace(" ", "")
            return text_response
        else:
            print("Error en la solicitud: ", response.stderr)
            return "false"
    except Exception as e:
        print(f"Error al enviar el ID con subprocess: {e}")
        return "false"

def sendToServerPIC(nom_foto):
    """Envia una imatge al servidor utilitzant curl."""
    try:
        response = subprocess.run(['curl', '-X', 'POST', '-F', f'file=@{nom_foto}', 'https://beta-bbdd.duckdns.org/photos/upload'], capture_output=True, text=True)

        if response.returncode == 0:
            # Procesar la respuesta
            text_response = response.stdout.strip()
            # Eliminar todos los espacios de la respuesta si es necesario
            text_response = text_response.replace(" ", "")
            return text_response
        else:
            print("Error enviant la imatge:", response.stderr)
            return "false"
    except Exception as e:
        print(f"Error al enviar la imatge amb subprocess: {e}")
        return "false"
