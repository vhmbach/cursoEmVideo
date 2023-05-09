import time
import pyautogui
from PIL import ImageGrab

def jump():
    # Simula uma pressão da tecla de espaço para fazer o dinossauro pular
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')

def duck():
    # Simula uma pressão da tecla de seta para baixo para fazer o dinossauro se agachar
    pyautogui.keyDown('down')
    time.sleep(0.05)
    pyautogui.keyUp('down')

def get_screen():
    # Captura uma imagem da tela do jogo
    screen = ImageGrab.grab()
    return screen

def is_game_over(screen):
    # Verifica se o jogo terminou, olhando para uma parte específica da tela
    game_over_box = (340, 190, 400, 230)
    game_over_region = screen.crop(game_over_box)
    game_over_image = game_over_region.convert('L')
    game_over_pixels = list(game_over_image.getdata())
    return sum(game_over_pixels) < 10000

def is_cactus(screen):
    # Verifica se um cacto está aparecendo na tela, olhando para uma parte específica da tela
    cactus_box = (190, 225, 250, 245)
    cactus_region = screen.crop(cactus_box)
    cactus_image = cactus_region.convert('L')
    cactus_pixels = list(cactus_image.getdata())
    return sum(cactus_pixels) < 2000

def main():
    # Aguarda três segundos para que o jogo carregue
    time.sleep(3)
    
    while True:
        # Captura uma imagem da tela do jogo
        screen = get_screen()

        # Verifica se o jogo terminou
        if is_game_over(screen):
            # Se o jogo terminou, reinicia o jogo
            pyautogui.click(x=530, y=310)
            time.sleep(0.5)
            pyautogui.press('space')

        # Verifica se há um cacto na tela
        elif is_cactus(screen):
            # Se houver um cacto, pula
            jump()

        # Se não houver um cacto, agacha-se
        else:
            duck()

        # Aguarda um curto período de tempo antes de verificar a tela novamente
        time.sleep(0.1)

if __name__ == '__main__':
    main()
