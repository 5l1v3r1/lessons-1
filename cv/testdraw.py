import pyautogui as py
import time

def mdrawTo(len,dx,dy):
    mtime = 0.05/200*len
    py.dragRel(dx, dy, mtime)
    

time.sleep(3)

lside = 400
lsteep = 5
py.dragRel(lside, 0, 1)
while True:
    mdrawTo(lside, 0, lside)
    mdrawTo(lside, -lside, 0)
    lside -= lsteep
    if lside < 0: break
    
    mdrawTo(lside , 0, -lside)
    mdrawTo(lside, lside, 0)
    lside -= lsteep
    if lside < 0: break
    
