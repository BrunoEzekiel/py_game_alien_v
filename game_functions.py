# Description: Funções do jogo
# autor: Bruno Ezequiel
import sys
import pygame
# respond to keypresses and mouse events


def check_keydown_events(ship, event):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(ship, event):
    
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship,):
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ship, event)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)      
        

def update_screen(ai_settings, screen, ship):
    ''' atualiza as imagens na tela e alterna para a nova tela '''
    # redesenha a tela a cada passagem pelo loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # faz a tela mais recentemente desenhada visivel
    pygame.display.flip()