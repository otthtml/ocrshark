import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from pytesseract import Output
from PIL import Image
import pyautogui
from time import sleep


#to find the required mouse positions

# import pyautogui
# pyautogui.displayMousePosition()

pyautogui.FAILSAFE = True
c1x, c1y = 1473, 525
c2x, c2y = 1481, 577
c3x, c3y = 1169, 487

delay = 0.2
sl = -75
linkedInx, linkedIny = 1187, 338 # linkedin adaptation


def takeSS():
    """
    Function that returns screenshot
    """
    sleep(delay)
    myScreenshot = pyautogui.screenshot()
    # return myScreenshot
    myScreenshot.save(r'.\ss.png')



def main(string1):
    sleep(delay)
    takeSS()
    p = Image.open("ss.png") #open the screenshot
    d = tess.image_to_data(p, output_type=Output.DICT, lang='por') #use tess to read and convert to dict
    n_boxes = len(d['level']) 
    count = 0
    # with open('output.txt', 'w', encoding='utf-8') as arq:
    #     arq.write(str(d))
    for i in range(n_boxes): #loop through the entire dict
        if string1 in d['text'][i]: #if string1 is in dict:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            count += 1
            act(x, y)
            return True


def act(x, y):
    mouseAction(x, y)
    mouseAction(c1x, c1y)
    mouseAction(c2x, c2y)
    mouseAction(c3x, c3y)


    
 
def mouseAction(x, y):
    sleep(delay)
    pyautogui.moveTo(x, y)
    sleep(delay)
    pyautogui.click()
    sleep(delay)
    pyautogui.scroll(sl)




if __name__=="__main__":
    sleep(2)
    # print(pyautogui.position())
    while True:
        try:
            if not main("Adicionar"): #for facebook
                act(c1x, c1y)
            # if not main("Next"):
            #     if not main("Conectar"):
            #         act(c1x, c1y)

        except pyautogui.FailSafeException:
            print("pyautogui FailSafeException!")
            break
