print("\"Vampire Hunters 3: Auto Escape\" Running...")
import string
import pyautogui, time, os, cv2, pytesseract
from pynput.keyboard import Key, Controller
from PIL import ImageGrab, Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
keyboard = Controller()

if __name__ == "__main__":
    time.sleep(1)
    while 1:
        # Manually found coordinates for the top and bottom of the escape input.
        img = ImageGrab.grab((944,798,983,843))
        img.save("escape.png")
        img.close()
        img = cv2.imread("escape.png")
        # Get the text from the image.
        text = pytesseract.image_to_string(Image.open("escape.png"),config="--psm 13")
        if text == "": print ("No text detected.")
        #print(text)
        num = None
        try:
            num = int(text)
            print("Number: " + str(num))
            # Execute escape
            keyboard.press(str(num))
            keyboard.release(str(num))
        except Exception as err:
            print("E" + str(err))
            print("Not a number... Skipping.")
        time.sleep(0.05)


# TODO: RUN!77