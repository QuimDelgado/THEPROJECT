#!/usr/bin/env python3
"""
i2c.py
Quim Delgado
"""

import board
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import textwrap
import time

class Display:
    def __init__(self, address=0x3C, width=128, height=64, font_path='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', font_size=15):
        self.i2c = board.I2C()  # Inicia la comunicación I2C
        self.oled = adafruit_ssd1306.SSD1306_I2C(width, height, self.i2c, addr=address)  # Configura el display OLED
        self.font_path = font_path
        self.font_size = font_size
        self.width = width
        self.height =    height

    def clear_display(self):
        """Limpia el display."""
        self.oled.fill(0)
        self.oled.show()

    def draw_text(self, text, font_size=None):
        """Dibuja texto en el display."""
        self.clear_display()
        if font_size is None:
            font_size = self.font_size
        font = ImageFont.truetype(self.font_path, font_size)
        image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(image)
        wrapped_text = textwrap.fill(text, width=14)
        lines = wrapped_text.split('\n')
        y = 0
        for line in lines:
            draw.text((0, y), line, font=font, fill=255)
            y += font.getsize(line)[1]
        self.oled.image(image)
        self.oled.show()

    def show_image(self, image_path="./foto_capturada.jpg"):
        """Muestra una imagen en el display."""
        try:
            image = Image.open(image_path)
            image = image.convert("L")
            image = image.resize((self.width, self.height))
            image = image.convert("1")
            self.oled.image(image)
            self.oled.show()
        except Exception as e:
            print(f"Error al mostrar la imagen: {e}")

    def draw_bitmap(self, bitmap_bytes):
        """
        Dibuja un mapa de bits en el display a partir de un array de bytes.
        """
        image = Image.new('1', (self.width, self.height))
        draw = ImageDraw.Draw(image)

        x = 0
        y = 0

        for byte in bitmap_bytes:
            for bit in range(8):
                if byte & (1 << (7-bit)):
                    draw.point((x, y), fill=255)
                x += 1
                if x >= self.width:
                    x = 0
                    y += 1

        self.oled.image(image)
        self.oled.show()


instancia_display = Display() # Instancia global para ser usada a través de los módulos

if __name__ == "__main__":
    try:
        while True:
            print("\n")
            print("Seleccione una función:")
            print("1. Mostrar texto")
            print("2. Mostrar imagen")
            print("3. Mostrar mapa de bits")
            print("4. Salir")

            seleccion = input("Opción: ")

            if seleccion == "1":
                text = input("Ingrese el texto: ")
                instancia_display.draw_text(text)
            elif seleccion == "2":
                instancia_display.show_image()
            elif seleccion == "3":
                bitmap_bytes = input("Ingrese el mapa de bits como una secuencia de bytes separados por comas: ")
                bitmap_bytes = [int(byte) for byte in bitmap_bytes.split(',')]
                instancia_display.draw_bitmap(bitmap_bytes)
            elif seleccion == "4":
                break
            else:
                print("Opción no reconocida")

    except KeyboardInterrupt:
        print("Programa terminado por el usuario.")
    finally:
        instancia_display.clear_display()  # Limpia la pantalla al finalizar
