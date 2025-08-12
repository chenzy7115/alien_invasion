import sys
import pygame

from settings import Settings
from ship import Ship

# print(pygame.__version__)


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()  # 实例化Settings类

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("外星人入侵 Alien Invasion")

        self.ship = Ship(self)  # 实例化Ship类

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            self.ship.update()  # 调用Ship类的update()方法,移动飞船

            # Redraw the screen during each pass through the loop.
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:  # 响应退出事件
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 响应按键事件
                if event.key == pygame.K_RIGHT:  # 按下右键
                    self.ship.moving_right = True  # 移动标志
                elif event.key == pygame.K_LEFT:  # 按下左键
                    self.ship.moving_left = True  # 移动标志
            elif event.type == pygame.KEYUP:  # 松开按键事件
                if event.key == pygame.K_RIGHT:  # 松开右键
                    self.ship.moving_right = False  # 移动标志
                elif event.key == pygame.K_LEFT:  # 松开左键
                    self.ship.moving_left = False  # 移动标志

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # 调用Ship类的blitme()方法
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
