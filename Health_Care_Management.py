from pygame import mixer
from datetime import datetime
from time import time

#   water(200 mL) in 25 min
#   Eyes in 30 min
#   Exercise in 45 min


def msc(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        query = input("Enter code to exit: ")
        if query == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("record_store.txt", "a") as file:
        file.write(f"{msg} is done at {datetime.now()}\n")


if __name__ == "__main__":
    init_water = time()
    init_eyes = time()
    init_exe = time()
    water = 30*60
    eyes = 60*60
    exe = 2*60*60

    while True:
        if time() - init_water > water:
            print("Drinking water Task.")
            msc("exer.mp3", "Drank")
            init_water = time()
            log_now("Water drank")
            n = int(input("Do you want to exit "))
            if n == 1:
                break

        if time() - init_eyes > eyes:
            print("Eyes")
            msc("eyes.mp3", "Eye")
            init_eyes = time()
            log_now("Eyes movement")

        if time() - init_exe > exe:
            print("Exercise")
            msc("exer.mp3", "Exercise")
            init_exe = time()
            log_now("Exercise")

    with open("record_store.txt") as f:
        a = f.read()
        print(a)
