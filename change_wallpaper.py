from PIL import Image
import os
import pyautogui
import getpass

print("***************************************************************************************************")
print("*   /$$$$$$                      /$$             /$$   /$$            /$$$$$$  /$$$$$$$   /$$$$$$ *")
print("*  /$$__  $$                    | $$            |__/  | $$           /$$__  $$| $$__  $$ /$$__  $$*")
print("* | $$  \__/ /$$   /$$  /$$$$$$$| $$   /$$       /$$ /$$$$$$        | $$  \__/| $$  \ $$| $$  \__/*")
print("* |  $$$$$$ | $$  | $$ /$$_____/| $$  /$$/      | $$|_  $$_/        | $$      | $$$$$$$/|  $$$$$$ *")
print("*  \____  $$| $$  | $$| $$      | $$$$$$/       | $$  | $$          | $$      | $$____/  \____  $$*")
print("*  /$$  \ $$| $$  | $$| $$      | $$_  $$       | $$  | $$ /$$      | $$    $$| $$       /$$  \ $$*")
print("* |  $$$$$$/|  $$$$$$/|  $$$$$$$| $$ \  $$      | $$  |  $$$$/      |  $$$$$$/| $$      |  $$$$$$/*")
print("*  \______/  \______/  \_______/|__/  \__/      |__/   \___/         \______/ |__/       \______/ *")
print("***************************************************************************************************")
print("")
print("[*] This program will change the wallpaper of your computer since CPS doesn't let you!")
path = input("[?] Put the file location of the image here(Must be full file location, you can drag and drop): ")

width, height = pyautogui.size()
size = (width, height)

name = "CachedImage_" + str(width) + "_" + str(height) + "_POS4.jpg"

user = getpass.getuser()

image = Image.open(path)
image = image.resize(size)
cached = Image.open("C:\\Users\\" + user +"\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\CachedFiles\\" + name)
cached.paste(image, (0,0))

os.remove("C:\\Users\\" + user +"\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\CachedFiles\\" + name)
cached = cached.save("C:\\Users\\" + user +"\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\CachedFiles\\" + name)