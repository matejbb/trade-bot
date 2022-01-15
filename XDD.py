import pyautogui as pag
import time

firstcandle = 0
lastcandle = 0
xd = False

quantity = float(input("xd: "))

stoploss = []

def clickOn(directory,click=True):
    pag.moveTo(pag.locateCenterOnScreen(directory,confidence=0.8))
    if click == True:
        pag.click()

def getRSI(posit):
    for v in range(658,930):
            if pag.pixel(posit,v) == (66, 189, 168):
                y = "zelena"
                return True
            elif pag.pixel(posit,v) == (255, 255, 255):
                y = "biela"
                return False

def getEMA(posit):
    global firstcandle
    global lastcandle
    global xd
    xd = False
    for i in range(110,650):
        if xd == False:
            if pag.pixel(pos,i) == (38, 166, 154):
                firstcandle = i
                xd = True
            elif xd == True and pag.pixel(pos,i) == (38, 166, 154):
                lastcandle = i
                return True
            elif pag.pixel(pos,i) == (239, 83, 80):
                firstcandle = i
                return True
            elif pag.pixel(pos,i) == (255, 255, 255):
                return False
        elif xd == True:
            if pag.pixel(pos,i) == (38, 166, 154):
                lastcandle = i
            else:
                return True

def findStopLoss(posit):
    global stoploss
    stoploss = []
    for i in range(110,650):
        if pag.pixel(posit,i) == (30, 83, 229):
            stoploss.append(i)

while True:
    if pag.locateOnScreen("C:/Users/seker/Desktop/xddddd.png") is not None:
        position = pag.locateCenterOnScreen("C:/Users/seker/Desktop/xddddd.png")
        pos = int(position[0])

        if getRSI(pos) is True:
            if getEMA(pos) is True:
                clickOn("C:/Users/seker/Desktop/long.png")
                pag.moveTo(pos,firstcandle)
                pag.click()
                findStopLoss(pos)
                pag.moveTo(pos,stoploss[7]+3)
                pag.dragTo(pos, lastcandle, button='left',duration=1)
                pag.moveTo(pos-2, stoploss[1]+2)
                pag.dragTo(pos-2, firstcandle-(lastcandle-firstcandle)*2, button="left", duration=1)
                print("buy")
                pag.rightClick()
                time.sleep(0.2)
                pag.moveTo(pag.locateCenterOnScreen("C:/Users/seker/Desktop/create.png"))
                pag.click()
                time.sleep(0.2)
                pag.moveTo(pag.locateCenterOnScreen("C:/Users/seker/Desktop/units.png"))
                pag.doubleClick()
                pag.write(str(quantity))
                time.sleep(0.1)
                pag.moveTo(pag.locateCenterOnScreen("C:/Users/seker/Desktop/buy.png"))
                pag.click()
        else:
            print("dont buy")
        