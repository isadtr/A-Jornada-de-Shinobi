import pygame
from game import Game

class Menu:
    def __init__(self, window: pygame.Surface):
        """
        Representa o menu inicial do jogo.
        :param window: Superfície principal do jogo (janela).
        """
        self.window = window

    def run(self) -> None:
        """
        Loop principal do menu. Pode conter opções como "Iniciar Jogo", "Sair", etc.
        Aqui, vamos simplificar para iniciar o jogo quando uma tecla é pressionada.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # Ao pressionar qualquer tecla, iniciamos o jogo
                    game = Game(self.window)
                    game.run()

            # Desenha um fundo simples para o menu
            self.window.fill((50, 50, 50))
            pygame.display.flip()

        pygame.quit()
