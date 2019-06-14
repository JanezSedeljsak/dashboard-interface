import pyfirmata
from pyfirmata import Arduino, util

def turn0On(power):
    board = pyfirmata.Arduino("COM5")#/dev/ttyACM0
    led = board.get_pin('d:11:p')
    led.write(power)

def turn1On(power):
    board = pyfirmata.Arduino("COM5")#/dev/ttyACM0
    led = board.get_pin('d:10:p')
    led.write(power)      
    
