import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()  # 实例化Settings类

        self.screen = pygame.display.set_mode(
            # (0, 0), pygame.FULLSCREEN  # 全屏模式
            (self.settings.screen_width, self.settings.screen_height)  # 窗口模式
        )
        # 获取屏幕尺寸width和height,并设置窗口大小
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("外星人入侵 Alien Invasion")

        self.ship = Ship(self)  # 实例化Ship类
        self.bullets = pygame.sprite.Group()  # 创建一个空编组,用于存储所有的子弹

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            self.ship.update()  # 调用Ship类的update()方法,移动飞船
            self._update_bullets()  # 调用_update_bullets()方法,更新子弹

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:  # 响应退出事件
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 响应按键事件
                self._check_keydown_events(event)
                # print(event.key)  # 打印按键的键值
            elif event.type == pygame.KEYUP:  # 松开按键事件
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:  # 按下右键
            self.ship.moving_right = True  # 移动标志
        elif event.key == pygame.K_LEFT:  # 按下左键
            self.ship.moving_left = True  # 移动标志
        elif event.key == pygame.K_SPACE:  # 按下空格键,发射子弹
            self._fire_bullet()
        elif event.key == pygame.K_q:  # 按下q键,退出游戏
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:  # 松开右键
            self.ship.moving_right = False  # 移动标志
        elif event.key == pygame.K_LEFT:  # 松开左键
            self.ship.moving_left = False  # 移动标志

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if (
            len(self.bullets) < self.settings.bullets_allowed
        ):  # 限制子弹数量,避免子弹过多

            new_bullet = Bullet(self)  # 实例化Bullet类,创建子弹对象
            self.bullets.add(new_bullet)  # 将子弹对象添加到编组bullets中

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        # Update bullets positions.
        self.bullets.update()  # 调用Bullet类的update()方法,移动子弹

        for (
            bullet
        ) in self.bullets.copy():  # 遍历编组bullets中的所有子弹对象,检查是否飞出屏幕
            if bullet.rect.bottom <= 0:  # 子弹飞出屏幕
                self.bullets.remove(bullet)  # 删除子弹对象
        print(len(self.bullets))  # 打印编组bullets中的子弹数量

        # Redraw the screen during each pass through the loop.
        self._update_screen()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # 调用Ship类的blitme()方法
        for (
            bullet
        ) in (
            self.bullets.sprites()
        ):  # 遍历编组bullets中的所有子弹对象,调用Bullet类的draw_bullet()方法
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
