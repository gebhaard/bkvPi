import os

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
BUTTONS = {
    18: '/path/to/sound/file1.wav',
    23: '/path/to/sound/file2.wav',
    24: '/path/to/sound/file3.wav',
}
for button_pin in BUTTONS:
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def play_sound(sound_file):
    os.system('aplay ' + sound_file)

def button_callback(channel):
    if channel in BUTTONS:
        print("Button {} was pressed!".format(channel))
        play_sound(BUTTONS[channel])

for button_pin in BUTTONS:
    GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback, bouncetime=300)

try:
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
