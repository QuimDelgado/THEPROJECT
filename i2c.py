# i2c.py
import board
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import textwrap

class OledDisplay:
    def __init__(self, address=0x3C, width=128, height=64, font_path='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', font_size=15):
        self.i2c = board.I2C()
        self.oled = adafruit_ssd1306.SSD1306_I2C(width, height, self.i2c, addr=address)
        self.font = ImageFont.truetype(font_path, font_size)
        self.width = width
        self.height = height

    def clear_display(self):
        """Limpia el display."""
        self.oled.fill(0)
        self.oled.show()

    def draw_text(self, text):
        """Dibuja texto en el display, con ajuste automático y salto de línea."""
        self.oled.fill(0)
        image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(image)

        wrapped_text = textwrap.fill(text, width=20)
        lines = wrapped_text.split('\n')
        y = 0
        for line in lines:
            draw.text((0, y), line, font=self.font, fill=255)
            y += self.font.getsize(line)[1]

        self.oled.image(image)
        self.oled.show()

if __name__ == "__main__":
    display = OledDisplay()
    display.draw_text("Hola, mundo!")
