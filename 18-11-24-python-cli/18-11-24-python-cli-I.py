import os

os.system("sudo apt update")
os.system("touch text.txt")
import random
num = random.randint(1,6)
if num == 4:#russian roulette
    os.system("os reboot")