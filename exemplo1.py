import pyautogui
import time

#aguarde 5s
time.sleep(5)

#Obtenha e imprima as dimensões da tela

largura, altura = pyautogui.size()
print(f"A largura da tela é{largura} e a altura da tela é{altura}")

#Mover o mouse para as coordenada (x,y) e clicar em algo

pyautogui.moveTo(100, 100, duration=1.5)
pyautogui.click()

#Digite usando um teclado virtual

pyautogui.typewrite("hello World")