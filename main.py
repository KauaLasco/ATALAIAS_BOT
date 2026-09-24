import pyautogui
import random
import time

ALVO_X_1, ALVO_Y_1 = 849, 803 #ÁREA ESCREVER COMENTÁRIO
ALVO_X_2, ALVO_Y_2 = 1226, 801 #ÁREA ENVIAR COMENTÁRIO
TEXTO_ESCREVER = 'ATALAIAS!'

pyautogui.FAILSAFE = True

def delay_humano(min_seg, max_seg):
    time.sleep(random.uniform(min_seg, max_seg))

def click_humano(x, y):
    jitter_x = x + random.randint(-5, 5)
    jitter_y = y + random.randint(-5, 5)
    
    duration = random.uniform(0.5, 1.5)
    pyautogui.click(jitter_x, jitter_y, duration=duration)

def run_bot():
    try:
        input_usuario = input('Quantidade de execuções: ')
        iteracoes = int(input_usuario)

        for i in range(iteracoes):
            print(f"Execução {i + 1}...")

            delay_humano(1, 2)

            click_humano(ALVO_X_1, ALVO_Y_1)
            
            for letra in TEXTO_ESCREVER:
                pyautogui.write(letra)
                time.sleep(random.uniform(0.1, 0.2)) #DELAY ENTRE LETRAS

            delay_humano(0.5, 1.22)

            click_humano(ALVO_X_2, ALVO_Y_2)

            print("Aguardando próximo ciclo...")
            delay_humano(1.5, 4)

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    run_bot()