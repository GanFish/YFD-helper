import pyautogui
import keyboard
import pygetwindow as gw
import time
import easygui

F3 = False
smallyuan = [(255,232,135),996,1268]
typeways = ["退出","小猿抢麦器模式模式","开发人员模式"]


def f3(x,y):
    colors = get_color_at_point(861,798)
    print("color" + str(colors) + "position:(x,yq)" + str(x) + " "+ str(y))
def get_color_at_point(x, y):
    return pyautogui.screenshot().getpixel((x, y))
typeway = easygui.buttonbox(msg="请选择使用模式", title="提示", choices=typeways)
print(typeway)
typeway = typeways.index(typeway)
if typeway == 4:
    F3 = True
easygui.msgbox(msg=typeways[typeway]+"\n点击OK键开始进行使用（q键强制退出）", title="提示")
while True:
    top_left_x,top_left_y = pyautogui.position()
    if F3==1:
        f3(top_left_x,top_left_y)
    needto_check_color = (231, 244, 253)
    color_for_password = get_color_at_point(861, 798)
    if get_color_at_point(987 ,1269) == (255, 232, 135) and 2==typeway:
        pyautogui.moveTo(987 ,1269, duration=0)
        pyautogui.click()
    if typeway == 0:
        exit(0)
    if keyboard.is_pressed('q') or keyboard.is_pressed('Q'):
        exit(0)
