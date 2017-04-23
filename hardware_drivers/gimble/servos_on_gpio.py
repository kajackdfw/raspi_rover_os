import RPi.GPIO as GPIO

class Gimbal:

    settings = {}
    uis = {}

    try:
        GPIO.setmode(GPIO.BOARD)
        uis['gimbal_horz'] = 'active'
        uis['gimbal_vert'] = 'active'
    except NameError:
        print(" - No Rpi GPIO library available.")
        settings['drive'] = 'disabled'
        uis['drive'] = 'disabled'

    def __init__(self, start_settings):
        self.settings['gimbal_horz'] = start_settings['gimbal_horz_servo_gpio']
        self.settings['gimbal_vert'] = start_settings['gimbal_vert_servo_gpio']

        if not self.settings['gimbal_horz'] == 'False':
            self.settings['gimbal_horz'] = int(self.settings['gimbal_horz'])
            self.settings['gimbal_horz_full_down'] = start_settings['gimbal_horz_full_down']
            self.settings['gimbal_horz_center'] = start_settings['gimbal_horz_full_down']
            self.settings['gimbal_horz_full_up'] = start_settings['gimbal_horz_full_down']
            self.settings['gimbal_horz_up'] = start_settings['gimbal_horz_full_down']
            self.settings['gimbal_horz_down'] = start_settings['gimbal_horz_full_down']
            self.uis['gimbal_horz'] = 'active'
        else:
            self.settings['gimbal_horz'] = False
            self.uis['gimbal_horz'] = 'disabled'

        if not self.settings['gimbal_vert'] == 'False':
            self.settings['gimbal_vert'] = int(self.settings['gimbal_vert'])
            self.settings['gimbal_vert_full_down'] = start_settings['gimbal_vert_full_down']
            self.settings['gimbal_vert_center'] = start_settings['gimbal_vert_full_down']
            self.settings['gimbal_vert_full_up'] = start_settings['gimbal_vert_full_down']
            self.settings['gimbal_vert_up'] = start_settings['gimbal_vert_full_down']
            self.settings['gimbal_vert_down'] = start_settings['gimbal_vert_full_down']
            self.uis['gimbal_vert'] = 'active'
        else:
            self.settings['gimbal_vert'] = False
            self.uis['gimbal_vert'] = 'disabled'

    def get_uis(self):
        return self.uis