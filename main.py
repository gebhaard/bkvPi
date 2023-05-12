import os

import RPi.GPIO as GPIO

path = '/home/gebhardm/Documents/sounds/'

def play_sound(sound_file):
    if play_sound.current_file is not None:
        print("You can't play multiple sounds at once!")
        return
    else:
        play_sound.current_file = sound_file
        os.system('aplay ' + path + sound_file)
        play_sound.current_file = None

def button_callback(channel):
    if channel in BUTTONS:
        print(f'Button {channel} was pressed!')
        play_sound(BUTTONS[channel])

print('Initializing...')
play_sound.current_file = None
GPIO.setmode(GPIO.BCM)
BUTTONS = {    
    18: 'sample-3s.wav',
    22: '',
    23: 'file2.wav',
    24: 'file3.wav',
    25: '',
    27: '',
}
print('Initializing buttons...')
for button_pin in BUTTONS:
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print(f'Button {button_pin} initialized.')

for button_pin in BUTTONS:
    GPIO.add_event_detect(button_pin,
                          GPIO.FALLING,
                          callback=button_callback,
                          bouncetime=300)

try:
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
