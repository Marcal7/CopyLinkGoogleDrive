import pyautogui
import time

print("Move o cursor até o local desejado e pressione Ctrl+C para parar.")
while True:
    x, y = pyautogui.position()
    print(f"Posição atual do mouse: x={x}, y={y}", end="\r")
