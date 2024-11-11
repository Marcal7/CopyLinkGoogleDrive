import pyautogui
import pyperclip
import time

def link():
    # Passo 1: Clica no botão "Compartilhar"
    pyautogui.click(x=1866, y=145)  # Ajuste essas coordenadas para o botão "Compartilhar"
    pyautogui.sleep(0.2)

    # Passo 2: Clica em "Copiar link"
    pyautogui.click(x=1777, y=199)  # Ajuste as coordenadas para o botão "Copiar link"
    pyautogui.sleep(0.2)

    # Passo 3: Tenta pegar o link copiado da área de transferência
    linkimage = pyperclip.paste()
    attempts = 3  # Número de tentativas para capturar o link

    # Checa se o link foi copiado corretamente; tenta até 'attempts' vezes se necessário
    while not linkimage and attempts > 0:
        time.sleep(0.2)  # Espera um pouco antes de tentar novamente
        linkimage = pyperclip.paste()
        attempts -= 1

    # Passo 4: Passa para a próxima foto
    pyautogui.press('right')
    pyautogui.sleep(1)

    # Retorna o link copiado
    if linkimage:
        return linkimage
    else:
        print("Erro ao copiar o link.")
        return None
