import pyautogui
import time

# --- INÍCIO DAS CONFIGURAÇÕES ---

# Substitua pelas coordenadas X e Y desejadas
coordenada_x = 1373
coordenada_y = 287

# Intervalo de tempo entre os cliques em segundos
intervalo_clique = 15

# --- FIM DAS CONFIGURAÇÕES ---

print("O programa de autoclick foi iniciado.")
print(f"A cada {intervalo_clique} segundos, um clique será dado em X={coordenada_x}, Y={coordenada_y}.")
print("Para parar o programa, feche esta janela do terminal ou pressione Ctrl+C.")

try:
    while True:
        pyautogui.click(coordenada_x, coordenada_y)
        time.sleep(intervalo_clique)
except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")