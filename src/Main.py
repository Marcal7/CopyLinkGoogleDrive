import numpy as np
import pyautogui

import GetLink

n = 100
listlink = []

print('Iniciando em 5 seg..')
pyautogui.sleep(5)

print('Iniciando')
for i in range(n):
    linkimage = GetLink.link()
    listlink.append(linkimage)

print(listlink)
# Converte listlink para um array NumPy de strings
listlink = np.array(listlink, dtype=str)

# Salva a lista de links em um arquivo de texto com formato string
np.savetxt("ListLink.txt", listlink, fmt='%s')

