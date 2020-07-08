import pyautogui
from time import sleep
from msvcrt import getch

pyautogui.FAILSAFE = True
# 基準点（左上の土を基準点とする）
basePoint = pyautogui.locateOnScreen(
    'img/base_point.png', grayscale=True, confidence=0.980)
cBasePoint = pyautogui.center(basePoint)
print("見つけました")
print(cBasePoint)
#print()
#pyautogui.click(cBasePoint.x+1030,cBasePoint.y+655)
checkPoints = [(1030, 523)
#            (1030, 403)
#            ,(1030, 536)
#            ,(1030, 655)
              ]

#im = pyautogui.screenshot(region=(cBasePoint[0], cBasePoint[1], 1130, 755))
#im.save('filename.png')

#以下繰り替えし処理、モグラの座標の位置を特定し土か犬以外ならクリック
while True:
    #スクリーンショット取得
#    pyautogui.moveTo(1130, 755)
    im = pyautogui.screenshot(region=(cBasePoint[0], cBasePoint[1], 1130, 755))
'''
    im.save('filename.png')
    pyautogui.press('up')
    sleep(1.5)
    pyautogui.press('down')
    sleep(1.5)
'''
    #7つの座標の文ループする
    for point in checkPoints:
        #指定された座標の色をcolorに代入する
        color = im.getpixel(point)
        colorR = color[0]
        colorG = color[1]
        colorB = color[2]
        print(color)
        sleep(2)
#        pyautogui.click(x=cBasePoint[0] + point[0],y=cBasePoint[1] + point[1])
#        sleep(2)
#        if colorR == 85 and colorG == 134 and colorB == 155:
'''
        if colorR == 0 and colorG == 0 and colorB == 0:
            pyautogui.click(x=cBasePoint[0] + point[0], y=cBasePoint[1] + point[1])
            pyautogui.press('up')
            sleep(0.5)
            pyautogui.press('down')
'''         

        


'''
    pyautogui.click(x=cBasePoint[0] + 1030,y=cBasePoint[1] + 403)
    sleep(0.3)
    pyautogui.click(x=cBasePoint[0] + 1030,y=cBasePoint[1] + 536)
    sleep(0.3)
    pyautogui.click(x=cBasePoint[0] + 1030,y=cBasePoint[1] + 655)
    sleep(0.3)
'''

