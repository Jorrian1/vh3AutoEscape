print("\"Vampire Hunters 3: Auto Escape (Version 2)\" Running...")
import time, os, cv2
from pynput.keyboard import Key, Controller
from PIL import ImageGrab, Image

keyboard = Controller()

if __name__ == "__main__":
    time.sleep(1)
    while 1:
        # Manually found coordinates for the top and bottom of the escape input.
        img = ImageGrab.grab((944,798,983,843))
        img.save("escape.png")
        img.close()
        img = cv2.imread("escape.png")
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        # Get the average color of the escape input.
        colors = []
 
        for i in range(img.shape[0]): # loop each row of pixels. 
            for j in range(img.shape[1]): # loop each pixel in row
                colors.append(img[i,j])

        r_sum = 0
        g_sum = 0
        b_sum = 0
        for color in colors:
            r_sum += color[0]
            g_sum += color[1]
            b_sum += color[2]
        prod = img.shape[0] * img.shape[1]
        avg_color = [r_sum//prod,g_sum//prod,b_sum//prod]
        print("Average RGB Value: " + str(avg_color))
        output = ""
        if avg_color == [77,90,179]: output = "w"
        elif avg_color == [169,150,48]: output = "a"
        elif avg_color == [167,48,101] or avg_color == [168,48,101]: output= "s"
        elif avg_color == [69,167,53]: output = "d"
        elif avg_color == [41,144,162] or avg_color == [41,143,162]: output = Key.space
        print("Output: " + str(output))
        if output != "":
            keyboard.press(output)
            keyboard.release(output)

        #time.sleep(0.01)
