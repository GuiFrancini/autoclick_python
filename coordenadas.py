import pyautogui
import time

print("Posicione o mouse sobre o local desejado em 5 segundos...")
time.sleep(5)

posicao_atual = pyautogui.position()
print(f"As coordenadas do mouse são: X={posicao_atual.x}, Y={posicao_atual.y}")