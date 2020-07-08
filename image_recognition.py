import pyautogui
from time import sleep
def operation():
    pyautogui.press('down')
    sleep(0.31)
    pyautogui.press('up')

basePoint = pyautogui.locateOnScreen(
    'img/base_point.png', grayscale=True, confidence=0.980)
cBasePoint = pyautogui.center(basePoint)
print("見つけました")
level = 0.95
Lx = cBasePoint[0]+900
Ly = cBasePoint[1]+240
Rx = 1270
Ry = 430
range_list = [
              440,
              410,
              410,
              410,
              440,
              440,
              440,
]
level_list = [
              0.94,
              0.93,
              0.95,
              0.92,
              0.95,
              0.95,
              0.95,
]
name_list = [
             'img/hole_v3.png',
             'img/water_v2.png',
             'img/color_cone.png',
             'img/no_entry.png',
             'img/asphalt_oil.png',
             'img/oil_vv3.png',
             'img/oil_v3.png',
             ]
#pyautogui.click(Rx, Ry)
#exit()

while True:
    for num in range(len(name_list)):
        #特定の範囲から画像と一致する座標（左上の座標と画像の高さ)を全て返す
        for pos in pyautogui.locateAllOnScreen(name_list[num], region=(Lx,Ly,Rx,range_list[num]), grayscale=True, confidence=level_list[num]):
            #座標の1点を取り出して画像の中心を取得する
            #cpos = pyautogui.center(pos)
            #画像の中心をクリックする
            #pyautogui.click(cpos)
            operation()
    
'''
#初期指定範囲
Lx = cBasePoint[0]+900
Ly = cBasePoint[1]+300
Rx = 1275
Ry = 755
'''