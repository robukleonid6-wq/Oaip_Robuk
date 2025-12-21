class smart_light:
    def __init__(self, brightness, color):
        self.brightness = brightness
        self.color = color
        self.__is_on = False
    
    def turn_on(self):
        self.__is_on = True
        print(f"лампа включена, цвет: {self.color}, яркость: {self.brightness}")
    
    def turn_off(self):
        self.__is_on = False
        print("лампа выключена")
    
    def set_color(self, new_color):
        self.color = new_color
        print(f"цвет изменен на {new_color}")

lampochka = smart_light(50, "белый")
lampochka.turn_on()
lampochka.set_color("синий")
lampochka.turn_off()