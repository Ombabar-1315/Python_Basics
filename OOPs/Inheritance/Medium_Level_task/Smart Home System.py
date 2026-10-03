class Device:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def show_devices(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)

    def turn_on(self):
        print("Device is Turn On.")

    def turn_off(self):
        print("Device is Turn Off.")

class SmartDevice(Device):

    def __init__(self, brand, model,wifi_name):
        super().__init__(brand, model)
        self.wifi_name = wifi_name

    def connect_wifi(self):
           super().show_devices()
           print("Wifi: ",self.wifi_name)
           print()
           print(f"Connected to {self.wifi_name}")


class SmartLight(SmartDevice):

    def __init__(self, brand, model, wifi_name,brightness):
        super().__init__(brand, model, wifi_name) 
        self.__brightness = brightness

    @property
    def brightness(self):
        return self.__brightness

    
    def set_brightness(self,value):
        if 0 <= value <= 100:
            self.__brightness = value
        else:
            print("Invalid Brightness.")
            print("Brightness must be between 0 and 100.")
    

    def show_devices(self):
         super().show_devices()
         print("Brightness: ",self.brightness)


S = SmartLight("Phillips","Hue_X1","Home-5G",70)
S.set_brightness(50)
S.show_devices()