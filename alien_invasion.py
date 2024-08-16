# descriçao: arquivo principal do jogo Alien Invasion
#autor: Bruno Ezequiel
# Importa o módulo sys
import pygame # Importa o módulo pygame
from settings import Settings # Importa a classe Settings
from ship import Ship  # Importa a classe Ship
import game_functions as gf # Importa o módulo game_functions


def run_game():

    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)

    while True:
        # responde a eventos de teclado e mouse
        gf.check_events(ship)
        ship.update()
        screen.fill(ai_settings.bg_color)
        gf.update_screen(ai_settings, screen, ship)
        ship.blitme()

        
        pygame.display.flip()
if __name__ == '__main__':
    run_game()# Chama a função run_game() para iniciar o jogo.
