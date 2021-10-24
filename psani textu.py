import keyboard
import time
import cv2
import pytesseract
import pyautogui


def main(mod,cas):
    ne = 0
    while True:
        if mod == 2: # radky text
            x1,y1,x2,y2 = 920,560,220,75
            y = 0
        if mod == 1: # normalni text
            x1,y1,x2,y2 = 635,363,798,396
            y = 0
        if mod == 3:
            x1,y1,x2,y2 = 635,450,801,300
            y = 1
        if mod == 4:
            x1,y1,x2,y2 = 552,335,801,398
            y = 0
        if mod == 6:
            if ne == 0:
                ne += 1
                print("Namir misi a dej enter")
                while True:
                    if keyboard.is_pressed("enter"):
                        w = pyautogui.position()
                        x1 = w.x
                        y1 = w.y
                        break
                time.sleep(1)
                while True:
                    if keyboard.is_pressed("enter"):
                        w = pyautogui.position()
                        x0 = w.x
                        y0 = w.y
                        break
                x2 = x0 - x1
                y2 = y0 - y1
                time.sleep(3)


        a = pyautogui.screenshot(region = (x1, y1, x2, y2))
        a.save("nevim.png")
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        img = cv2.imread("nevim.png")
        text = pytesseract.image_to_string(img,lang="ces")
        mystr =  " ".join(text.splitlines())
        keyboard.write(mystr,delay=0.01)


def zacatek():
    mod = int(input("Zadejte mod: "))
    cas = float(input("Za jakou dobu napsat jedno pismenko? : "))
    if mod != 6:
        while True:
            if keyboard.is_pressed("enter"):
                main(mod,cas)
    else:
        main(mod,cas)

zacatek()
