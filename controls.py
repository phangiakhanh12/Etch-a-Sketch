'''
A program that reads inputs from the Pico as
controls for an etch-a-sketch running on a laptop.
It sends those controls over USB to the etch-a-sketch
program to control a turtle.
'''
# some useful imports, feel free to modify
from picozero import Publisher, Button, Pot, PicoLED
from time import sleep

pub = Publisher()  # Lines 11 - 15: initialize the publisher, left and right potentiometers, button, and led
left_pot = Pot(28)
right_pot = Pot(27)
button = Button(15)
led = PicoLED()

while True: 
    '''
    Firstly, respectively store the values of the two pots into left_value and right_value.
    Then, generate a boolean variable as the state of the led.
    Next, check if the button is turned on, then the led is also on. Otherwise, the led stays off.
    Lastly, send these three values to the computer through the second USB port with a sleep(0.2)
    to ensure the gradual speed of the program.
    '''
    left_value = left_pot.read_position() 
    right_value = right_pot.read_position()
    button_state = int(button.is_pressed)
    if button_state:
        led.on()
    else:
        led.off()
    pub.send(left_value, right_value, button_state)
    sleep(0.2)
