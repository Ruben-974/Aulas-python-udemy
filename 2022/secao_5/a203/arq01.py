class Cam:

    def __init__(self, model):
        self.model = model
        self.film = False

    def to_record(self):
        if self.film:
            print(f'{self.model} is already film!')
            return
        self.film = True
        print(f'{self.model} is filming...')

    def stop_to_record(self):
        if self.film:
            print(f'{self.model} stopped recording!')
            self.film = False

    def photograph(self):
        if self.film:
            print(f"{self.model} doesn't take pictures during filming!")
            return
        print(f'{self.model} took a picture!')


cam1 = Cam('Sony')
cam1.to_record()
cam1.to_record()
cam1.to_record()
cam1.photograph()
cam1.stop_to_record()
cam1.photograph()
print()
cam2 = Cam('Canon')
cam2.to_record()
cam2.to_record()
cam2.photograph()
cam2.to_record()
cam2.stop_to_record()
cam2.photograph()
