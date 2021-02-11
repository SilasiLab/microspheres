import board
import neopixel
import time
import sys
import pigpio
from subprocess import PIPE, Popen
from datetime import datetime
import time
from neopixel import *
from rpi_ws281x import Adafruit_NeoPixel, Color

LED_COUNT = 16        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 200000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 250 # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False

pixels = neopixel.NeoPixel(board.D18, 16, bpp=3, brightness=1, auto_write=False)

# opens a preview window and then takes snapshot when user presses any key
while 1:
    no_input = True

    p = Popen(["raspistill", "-awb", "off", "-awbg", "1.0, 1.0",
            "-ss", "1000000", "-ex", "off", "-t", "10000000", "-rot", "89",
            "-vf", "-hf", "-o", savePath, "-p", "100, 100, 400, 300"
            ],stdin=PIPE, stdout=PIPE)
    while no_input:
        try:
            user_input = input()
            no_input = False
        except:
            pass
        time.sleep(1)
    
    if no_input == False:
        p.terminate()
        # change the color here
        pixels.fill((0, 0, 255))
        pixels.show()
        time.sleep(1)
        savePath = "/home/pi/Desktop/pi_brain/%s_%s.jpg" % (datetime.now().strftime("%m-%d-%Y_%H:%M:%S"), argument)
        print(savePath)
        p = Popen(["raspistill", "-awb", "off", "-awbg", "1.0, 1.0",
                "-ss", "1000000", "-ex", "off", "-t", "1000", "-rot", "89",
                "-vf", "-hf", "-o", savePath
                ],stdin=PIPE, stdout=PIPE)
        for line in p.stdout.readlines():
            print(line)
        time.sleep(1)
        pixels.fill((0, 0, 0))
