# no motors, this is a stationary rover or wildlife cam


class Motor:

    settings = {}
    uis = {}

    def __init__(self, start_settings):
        self.settings = {}
        self.settings['motor_mode'] = 'immobile'
        self.settings['drive'] = 'disabled'
        self.uis['motor'] = 'disabled'

    def get_uis(self):
        return self.uis
