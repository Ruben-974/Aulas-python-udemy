from main import LogFileMixin, LogPrintMixin

class Electronics:
    def __init__(self, is_on=False):
        self.is_on = is_on

    def power_on(self):
        if not self.is_on:
            self.is_on = True

    def power_off(self):
        if self.is_on:
            self.is_on = False

class SmartPhone(Electronics, LogFileMixin):

    def __init__(self, model):
        super().__init__()
        self.model = model

    def power_on(self):
        super().power_on()
        self.log_success(f'{self.model} is on: {self.is_on}')

    def power_off(self):
        super().power_off()
        self.log_error(f'{self.model} is on: {self.is_on}')


poco_f4 = SmartPhone('POCO F4')

poco_f4.power_on()
poco_f4.power_off()

