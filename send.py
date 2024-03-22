# send.py
import requests

def send_id(id):
    url = 'https://proxy-rfid.duckdns.org/procesar_datos'
    data = {'numero_rfid': id}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            # Eliminar espacios al principio y al final
            text_response = response.text.strip()
            # Si necesitas eliminar todos los espacios dentro de la cadena, puedes hacer:
            text_response = text_response.replace(" ", "")
            return text_response
        else:
            return "false"
    except Exception as e:
        print(f"Error al enviar el ID: {e}")
        return "false"
