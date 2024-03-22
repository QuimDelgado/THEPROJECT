import threading
import signal
from rfid import read
from send import send_id
from i2c import OledDisplay
import RPi.GPIO as GPIO

stop_event = threading.Event()
display = OledDisplay()

def rfid_thread_func(stop_event):
    try:
        while not stop_event.is_set():
            id, text = read()
            print(f"Llegit: ID={id}, Texto={text}")
            if not stop_event.is_set():  # Revisar nuevamente antes de hacer la solicitud
                response = send_id(id)
                if response != "false":
                    message = f"Usuari {response} reconegut"
                else:
                    message = "Usuari no reconegut"
                display.draw_text(message)
    except Exception as e:
        print(f"Error en RFID thread: \n{e}\n")
    finally:
        GPIO.cleanup()
        display.clear_display()

def signal_handler(sig, frame):
    print('Señal de interrupción recibida, deteniendo los hilos...')
    stop_event.set()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    rfid_thread = threading.Thread(target=rfid_thread_func, args=(stop_event,))
    rfid_thread.start()

    try:
        rfid_thread.join()
    except KeyboardInterrupt:
        stop_event.set()
        rfid_thread.join()
    finally:
        GPIO.cleanup()
        display.clear_display()
