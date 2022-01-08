# Ce capabilitati are un telefon:
# face poze,
# poti suna,
# navigare online
# GPS
# video
# Ce face un smart TV:
# navigare online
# cablu TV
# video
# Ce face smart-watch
# GPS
# poti suna
# numara pasii
# Health monitoring



#Definim capabilitatile de baza:

class GPS:
    def get_position(self):
        print("Getting the current position")

class Video:
    def run_video(self):
        print("Running current video")

class Calling:
    def calling_person(self):
        print("Call me maybe")

    def answer_call(self):
        print("Wrong number")

class Health:
    def heart_rate(self, number_beats_per_sec):
        if number_beats_per_sec >= 200:
            print("You are having a heart-attack")
        else:
            print("You are not dying")

    def numara_pasi(self, steps_perday):
        if steps_perday >= 10000:
            print("You are doing Great!")
        else:
            print("Keep walking!")



class CabluTV:
    def setare_canal(self):
        print("Canalul dorit este setat!")

class NavigareOnline:
    def open_chrome(self):
        print("Search Google")


class Foto:
    def take_picture(self):
        print("The picture was taken")



# Definirea claselor pe dispozitive prin inheritence

class Telefon(GPS, Video, Calling, NavigareOnline, Foto):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def take_picture(self):
        print("The HD photo was taken")

class SmartTV(Video, NavigareOnline, CabluTV):

    def __init__(self, brand, rezolutie):
        self.brand = brand
        self.rezolutie = rezolutie

    def setare_canal(self):
        print("Fara semnal- 404")

class SmartWatch(GPS, Calling, Health):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def calling_person(self):
        print("The person is not reachable. Try again later")

# Crearea obiectelor si invocarea (spiritelor) acestora

if __name__ == "__main__":

    tel = Telefon("hiphone", "12")
    tv = SmartTV("Samsung", "1024x1456")
    watch = SmartWatch("OPPO", "x1")

    tel.take_picture()
    tel.calling_person()
    tel.answer_call()

    print("===================")

    tv.setare_canal()

    print("===================")

    watch.calling_person()
    watch.heart_rate(234)
    watch.numara_pasi(5000)







