class Camera:

    def take_method(self):
        print("Taking a photo...")

class MusicPlayer:

    def play_music(self):
        print("Playing music...")

class SmartPhone(Camera,MusicPlayer):

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def show_phone(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        super().take_method()
        super().play_music()


brand = input("Enter Mobile brand: ")
model = input("Enter Mobile Model: ")
S = SmartPhone(brand,model)
S.show_phone()