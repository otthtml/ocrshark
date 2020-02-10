import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\Users\ottht\AppData\Local\Tesseract-OCR\tesseract.exe"
from pytesseract import Output
from PIL import Image
import pyautogui
from time import sleep



pyautogui.FAILSAFE = True
c1x, c1y = 1481, 577
c2x, c2y = 1473, 525
delay = 0.1
sl = -30


def takeSS():
    """
    Function that returns screenshot
    """
    sleep(0.5)
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'.\ss.png')



def main(string1):
    sleep(delay)
    takeSS()
    p = Image.open("ss.png") #open the screenshot
    # p = cv2.imread(r'.\ss.png')
    # p = cv2.cvtColor(p, cv2.COLOR_BGR2RGB)
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
    print(count)


def act(x, y):
    mouseAction(x, y)
    mouseAction(c1x, c1y)
    mouseAction(c2x, c2y)

    
 
def mouseAction(x, y):
    sleep(delay)
    pyautogui.moveTo(x, y)
    sleep(delay)
    pyautogui.click()
    sleep(delay)
    pyautogui.scroll(sl)




if __name__=="__main__":
    sleep(2)
    while True:
        try:
            pyautogui.scroll(sl)
            main("Adicionar")
        except pyautogui.FailSafeException:
            print("pyautogui FailSafeException!")
            break
