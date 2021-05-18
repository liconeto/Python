import pyautogui
import sys, time, msvcrt, random, time, os

# obs: Minha resolução de tela é 1366 x 768. Talvez será necessário adaptar as coordenadas
#      dos cliques automatizados para sua tela.

def jogar():
    time.sleep(0.5)
    pyautogui.click(670, 330)
    time.sleep(0.5)
    cartaEscolhida = random.randint(1,5) # Escolhe uma carta aleatória.
    if cartaEscolhida == 1:
        pyautogui.click(670, 330)
    elif cartaEscolhida == 2:
        pyautogui.click(717, 350)
    elif cartaEscolhida == 3:
        pyautogui.click(771, 351)
    elif cartaEscolhida == 4:
        pyautogui.click(815, 357)
    else:
        pyautogui.click(863, 350)
    time.sleep(7.5)
    pyautogui.click(760, 410)

def abrirJogo():                # Dá os cliques para abrir a extensão e o jogo de cartas.
    pyautogui.click(891, 537)
    time.sleep(1)
    pyautogui.click(694, 386)

def fecharJogo():               # Dá os cliques para fechar a extensão.
    time.sleep(0.5)
    pyautogui.click(880, 531)

def mudarAba():                 # Para mudar da aba do console para a aba do navegador.
    pyautogui.keyDown('alt',)
    pyautogui.press('tab')
    pyautogui.keyUp('alt')

def pararPrograma():
    timeout = 4
    startTime = time.time()
    inp = None
    print("Aperte qualquer tecla para continuar ou aguarde 4 segundos.")
    while True:
        if msvcrt.kbhit():
            inp = msvcrt.getch()
            break
        elif time.time() - startTime > timeout:
            break
    if inp:
        sys.exit()
    else:
       parar = False

clear = lambda: os.system('cls')  # Para limpar o console.

# Daqui pra frente é o programa funcionando.

print("Abra o canal na twitch e deixe em modo teatro. O programa iniciará em 10 segundos.")
time.sleep(10)
parar = False
while parar == False:
     abrirJogo()
     jogar()
     fecharJogo()
     mudarAba()
     clear()
     pararPrograma()
     mudarAba()